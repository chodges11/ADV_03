"""
main driver for a simple social network project
"""
# pylint: disable = import-error
# pylint: disable = unused-variable
# pylint:disable=unspecified-encoding

import csv
from loguru import logger
import peewee as pw
import socialnetwork_model as sm


def init_collections():
    """
    Creates and returns a new instance of the database.
    """
    sm.db.connect()
    sm.db.execute_sql('PRAGMA foreign_keys = ON;')
    sm.db.create_tables([
        sm.Users,
        sm.Status
    ])
    sm.db.close()


def load_users(filename):
    """
    Opens a CSV file with user data and adds it to a DB.
    """
    sm.db.connect()
    users = []
    try:
        with open(filename, 'r') as read_obj:
            reader = csv.DictReader(read_obj)
            for row in reader:
                users.append(row)

        try:
            for user in users:
                with sm.db.transaction():
                    new_user = sm.Users.create(
                        user_id=user[0],
                        user_name=user[1],
                        user_last_name=user[2],
                        user_email=user[3],
                    )
                    new_user.save()

        except OSError as error:
            logger.info(f"{type(error)}: {error}")
            return False

    except OSError as error:
        logger.info(f"{type(error)}: {error}")
        return False

    sm.db.close()
    return True


def load_status_updates(filename):
    """
    Opens a CSV file with status data and adds it to a DB.
    """
    sm.db.connect()
    status = []
    try:
        with open(filename, 'r') as read_obj:
            reader = csv.DictReader(read_obj)
            for row in reader:
                status.append(row)

        try:
            for stat in status:
                with sm.db.transaction():
                    new_status = sm.Status.create(
                        status_id=stat[0],
                        user_id=stat[1],
                        status_text=stat[2],
                    )
                    new_status.save()

        except OSError as error:
            logger.info(f"{type(error)}: {error}")
            return False

    except OSError as error:
        logger.info(f"{type(error)}: {error}")
        return False

    sm.db.close()
    return True


def add_user(user_id, user_name, user_last_name, email,):
    """
    Adds a new User to the database.
    """
    try:
        sm.db.connect()
        new_user = sm.Users.create(
            user_id=user_id,
            user_name=user_name,
            user_last_name=user_last_name,
            user_email=email,
        )
        new_user.save()
        sm.db.close()
        logger.info('Add User')
        return True

    except pw.PeeweeException as error:
        logger.info(f"{type(error)}: {error}")
        return False


def update_user(user_id, user_name, user_last_name, email):
    """
    Updates the values of an existing user
    """
    try:
        sm.db.connect()
        user = sm.Users.get(sm.Users.user_id == user_id)
        user.user_id = user_id
        user.user_name = user_name
        user.user_last_name = user_last_name
        user.user_email = email
        user.save()
        sm.db.close()
        logger.info('Update User')
        return True

    except pw.PeeweeException as error:
        logger.info(f"{type(error)}: {error}")
        return False


def delete_user(user_id):
    """
    Deletes a user from user_collection.
    """
    try:
        sm.db.connect()
        user = sm.Users.get(sm.Users.user_id == user_id)
        user.delete_instance()
        sm.db.close()
        logger.info('Delete User')
        return True

    except pw.PeeweeException as error:
        logger.info(f"{type(error)}: {error}")
        return False


def search_user(user_id):
    """
    Searches for a user in the DB.
    """
    try:
        sm.db.connect()
        user = sm.Users.get(sm.Users.user_id == user_id)
        sm.db.close()
        logger.info('Search User')
        return user

    except pw.PeeweeException as error:
        logger.info(f"{type(error)}: {error}")
        return None


def add_status(status_id, user_id, status_text):
    """
    Creates a new instance of UserStatus and stores it in
    status_collection(which is an instance of UserStatusCollection)

    Requirements:
    - status_id cannot already exist in status_collection.
    - Returns False if there are any errors (for example, if
      user_collection.add_status() returns False).
    - Otherwise, it returns True.
    """
    try:
        sm.db.connect()
        new_user = sm.Users.create(
            status_id=status_id,
            user_id=user_id,
            user_last_name=user_last_name,
            user_email=email,
        )
        new_user.save()
        sm.db.close()
        logger.info('Add User')
        return True

    except pw.PeeweeException as error:
        logger.info(f"{type(error)}: {error}")
        return False


def update_status(status_id, user_id, status_text, status_collection):
    """
    Updates the values of an existing status_id

    Requirements:
    - Returns False if there are any errors.
    - Otherwise, it returns True.
    """
    while status_collection.update_status(status_id,
                                          user_id,
                                          status_text
                                          ):
        return True
    return False


def delete_status(status_id, status_collection):
    """
    Deletes a status_id from user_collection.

    Requirements:
    - Returns False if there are any errors (such as status_id not found)
    - Otherwise, it returns True.
    """
    while status_collection.delete_status(status_id):
        return True
    return False


def search_status(status_id, status_collection):
    """
    Searches for a status in status_collection

    Requirements:
    - If the status is found, returns the corresponding
    UserStatus instance.
    - Otherwise, it returns None.
    """
    status_search_results = status_collection.search_status(status_id)
    if status_search_results.status_id is not None:
        return status_search_results
    return None

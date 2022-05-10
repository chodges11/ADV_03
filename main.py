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
    logger.info("Start Load Users")
    sm.db.connect()
    users = []
    try:
        with open(filename, 'r') as read_obj:
            reader = csv.DictReader(read_obj)
            for row in reader:
                users.append(row)

        for user in users:
            try:
                with sm.db.transaction():
                    new_user = sm.Users.create(
                        user_id=user['USER_ID'],
                        user_name=user['NAME'],
                        user_last_name=user['LASTNAME'],
                        user_email=user['EMAIL'],
                    )
                    new_user.save()

            except pw.PeeweeException as error:
                sm.db.close()
                logger.info(f"{type(error)}: {error}")
                return False

    except pw.PeeweeException as error:
        sm.db.close()
        logger.info(f"{type(error)}: {error}")
        return False

    sm.db.close()
    logger.info("End Load Users")
    return True


def load_status_updates(filename):
    """
    Opens a CSV file with status data and adds it to a DB.
    """
    logger.info("Start Load Status")
    sm.db.connect()
    status = []
    try:
        with open(filename, 'r') as read_obj:
            reader = csv.DictReader(read_obj)
            for row in reader:
                status.append(row)

        try:
            for stat in status:
                with sm.db.atomic():
                    new_status = sm.Status.create(
                        status_id=stat['STATUS_ID'],
                        user_id=stat['USER_ID'],
                        status_text=stat['STATUS_TEXT'],
                    )
                    new_status.save()

        except pw.PeeweeException as error:
            sm.db.close()
            logger.info(f"{type(error)}: {error}")
            return False

    except pw.PeeweeException as error:
        sm.db.close()
        logger.info(f"{type(error)}: {error}")
        return False

    sm.db.close()
    logger.info("End Load Status")
    return True


def add_user(user_id, user_name, user_last_name, email):
    """
    Adds a new User to the database.
    """
    try:
        sm.db.connect()
        new_user = sm.Users.create(
            user_id=user_id,
            user_name=user_name,
            user_last_name=user_last_name,
            user_email=email
        )
        new_user.save()
        sm.db.close()
        logger.info('Add User')
        return True

    except pw.PeeweeException as error:
        sm.db.close()
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

    except pw.DoesNotExist as error:
        sm.db.close()
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

    except pw.DoesNotExist as error:
        sm.db.close()
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

    except pw.DoesNotExist as error:
        sm.db.close()
        logger.info(f"{type(error)}: {error}")
        return None


def add_status(status_id, user_id, status_text):
    """
    Creates a new Status record and stores it in the DB.
    """
    try:
        sm.db.connect()
        new_status = sm.Status.create(
            status_id=status_id,
            user_id=user_id,
            status_text=status_text
        )
        new_status.save()
        sm.db.close()
        logger.info('Add Status')
        return True

    except pw.PeeweeException as error:
        sm.db.close()
        logger.info(f"{type(error)}: {error}")
        return False


def update_status(status_id, user_id, status_text):
    """
    Updates the values of an existing status, in the DB.
    """
    try:
        sm.db.connect()
        status = sm.Status.get(sm.Status.status_id == status_id)
        status.status_id = status_id
        status.user_id = user_id
        status.status_text = status_text
        status.save()
        sm.db.close()
        logger.info('Update Status')
        return True

    except pw.DoesNotExist as error:
        sm.db.close()
        logger.info(f"{type(error)}: {error}")
        return False


def delete_status(status_id):
    """
    Deletes a status from the DB.
    """
    try:
        sm.db.connect()
        status = sm.Status.get(sm.Status.status_id == status_id)
        status.delete_instance()
        sm.db.close()
        logger.info('Delete Status')
        return True

    except pw.DoesNotExist as error:
        sm.db.close()
        logger.info(f"{type(error)}: {error}")
        return False


def search_status(status_id):
    """
    Searches for a status in the DB.
    """
    try:
        sm.db.connect()
        status = sm.Status.get(sm.Status.status_id == status_id)
        sm.db.close()
        logger.info('Search status')
        return status

    except pw.DoesNotExist as error:
        sm.db.close()
        logger.info(f"{type(error)}: {error}")
        return None

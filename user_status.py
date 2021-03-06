"""
classes to manage the user status messages
"""
# pylint: disable=R0903

import sys
from loguru import logger


class UserStatus():
    """
    class to hold status message data
    """

    def __init__(self, status_id, user_id, status_text):
        self.status_id = status_id
        self.user_id = user_id
        self.status_text = status_text
        logger.add(sys.stderr, format="{time} {level} {message}",
                   filter="my_module", level="INFO")
        logger.add("log_file.log")
        logger.info('Created User Status')


class UserStatusCollection():
    """
    Collection of UserStatus messages
    """

    def __init__(self):
        self.database = {}
        logger.add(sys.stderr, format="{time} {level} {message}",
                   filter="my_module", level="INFO")
        logger.add("log_file.log")
        logger.info('Created User Status Collection')

    def add_status(self, status_id, user_id, status_text):
        """
        add a new status message to the collection
        """

        if status_id in self.database:
            # Rejects new status if status_id already exists
            logger.info('Did Not Add User Status: status_id already exists')
            return False
        new_status = UserStatus(status_id, user_id, status_text)
        self.database[status_id] = new_status
        logger.info('Add User Status')
        return True

    def update_status(self, status_id, user_id, status_text):
        """
        Updates a status message

        The new user_id and status_text are assigned to the existing message
        """

        if status_id not in self.database:
            # Rejects update if the status_id does not exist
            logger.info('Did Not Update User Status: status_id does not exist')
            return False
        self.database[status_id].user_id = user_id
        self.database[status_id].status_text = status_text
        logger.info('Updated User Status')
        return True

    def delete_status(self, status_id):
        """
        deletes the status message with id, status_id
        """
        if status_id not in self.database:
            # Fails if status does not exist
            logger.info('Did Not Delete User Status: status does not exist')
            return False
        del self.database[status_id]
        logger.info('Deleted User Status')
        return True

    def search_status(self, status_id):
        """
        Find and return a status message by its status_id

        Returns an empty UserStatus object if status_id does not exist
        """

        if status_id not in self.database:
            # Fails if the status does not exist
            logger.info(
                'Failed Search For User Status in Database: '
                'status does not exist')
            return UserStatus(None, None, None)
        logger.info('Successfully Searched for User Status')
        return self.database[status_id]

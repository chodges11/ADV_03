import os
import peewee as pw
from loguru import logger

file = 'socialnetwork.db'
if os.path.exists(file):
    os.remove(file)

db = pw.SqliteDatabase(file)


class DBModel(pw.Model):
    logger.info("Database class extending PeeWee Model.")

    class Meta:
        database = db


class Users(DBModel):
    """
        This class defines Users, which maintains specific of the users
        of our Social Network.
    """
    user_id = pw.CharField(primary_key=True, max_length=30)
    user_name = pw.CharField(max_length=30)
    user_last_name = pw.CharField(max_length=100)
    user_email = pw.CharField(max_length=100)


class Status(DBModel):
    """
        This class defines Status, which maintains specific of the statuses
        of the Users of our Social Network.
    """
    status_id = pw.CharField(primary_key=True)
    user_id = pw.ForeignKeyField(Users, null=False)
    status_text = pw.CharField()

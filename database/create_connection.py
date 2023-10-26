import sqlite3

from config.storage_config import STORAGE_CONFIG
from database import questions_table
from database import users_quiz_progress
from database import users_table


def create_db_connection():
    db_connection = sqlite3.connect(STORAGE_CONFIG['DB_NAME'], check_same_thread = False)

    questions_table.create_table(db_connection)
    users_quiz_progress.create_table(db_connection)
    users_table.create_table(db_connection)

    return db_connection
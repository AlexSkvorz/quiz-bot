from database import questions_table
from database import users_quiz_progress_table
from database import users_table


async def create_tables():
    await questions_table.create_table()
    await users_quiz_progress_table.create_table()
    await users_table.create_table()

from config.storage_config import STORAGE_CONFIG
from database.tables.questions_table import QuestionsTable
from database.tables.users_quiz_progress_table import UserQuizProgressTable
from database.tables.users_table import UsersTable


class QuizDatabase:
    def __init__(self):
        self._db_name = STORAGE_CONFIG['DB_NAME']
        self.questions_table = QuestionsTable()
        self.user_quiz_progress_table = UserQuizProgressTable()
        self.users_table = UsersTable()

    async def create_tables(self):
        await self.questions_table.create_table()
        await self.user_quiz_progress_table.create_table()
        await self.users_table.create_table()

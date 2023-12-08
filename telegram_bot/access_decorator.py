from functools import wraps
from constants import ADMIN


def admin_factory(database=None):
    def admin_required(func):
        @wraps(func)
        async def wrapper(message):
            user = await is_user_admin(user_id=message.from_user.id, database=database)
            if user:
                await func(message)

        return wrapper

    return admin_required


async def is_user_admin(user_id, database):
    user_role = await database.users_table.fetch_user_role(user_id=user_id)

    if user_role[0] == ADMIN:
        return True

    return False

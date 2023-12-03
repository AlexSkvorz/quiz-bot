from functools import wraps
from constants import ADMIN
from database.tables import users_table


def admin_required(func):
    @wraps(func)
    async def wrapper(message):
        user = await is_user_admin(user_id=message.from_user.id)
        if user:
            await func(message)

    return wrapper


async def is_user_admin(user_id):
    user_role = await users_table.fetch_user_role(user_id=user_id)

    if user_role[0] == ADMIN:
        return True

    return False

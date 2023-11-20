from database.questions_table import fetch_correct_answer


async def parse_user_choices(user_choice):
    user_choice = user_choice.split('_difficult=')
    difficult = user_choice[1]
    user_choice = user_choice[0].split('topic=')
    topic = user_choice[1]

    return topic, difficult


async def parse_user_answer(user_answer):
    correct_answer = False

    if 'correct' in user_answer:
        user_answer = user_answer.replace('_correct', '')
        completed, score = 1, 1
        correct_answer = True
    else:
        completed, score = 0, 0

    user_answer = user_answer.split('quiz_id=')
    quiz_id = int(user_answer[1])

    if not correct_answer:
        correct_answer = await fetch_correct_answer(quiz_id)

    return quiz_id, completed, score, correct_answer

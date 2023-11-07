import enum


class BotCommands(enum.Enum):
    START = 'start'
    SELECT_QUIZ = 'select_quiz'
    ADD_QUESTIONS = 'add_questions'
    VIEW_ACHIEVEMENTS = 'view_achievements'
    SELECT_TOPIC = 'select_topic'
    TO_START = 'to_start'
    SEND_QUESTION = 'send_question'
    SELECT_ANSWER = 'select_answer'
    SELECT_DIFFICULT = 'select_difficult'

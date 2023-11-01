import enum


class BotCommands(enum.Enum):
    START = 'start'
    SELECT_QUIZ = 'select_quiz'
    ADD_QUESTIONS = 'add_questions'
    VIEW_STATISTIC = 'view_statistic'
    SELECT_TOPIC = 'select_topic'
    TO_START = 'to_start'
    SEND_QUESTION = 'send_question'
    SELECT_ANSWER = 'select_answer'
    END_QUIZ = 'end_quiz'

import pymorphy2

morph = pymorphy2.MorphAnalyzer()


def get_word_form(quantity_unique_questions):
    word_form = morph.parse("вопросы")[0].make_agree_with_number(quantity_unique_questions).word
    return word_form



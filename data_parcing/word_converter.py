import pymorphy2

morph = pymorphy2.MorphAnalyzer()


def get_word_form(quantity, word):
    parsed_word = morph.parse(word)[0]
    agreed_word = parsed_word.make_agree_with_number(quantity)
    word_form = agreed_word.word
    return word_form

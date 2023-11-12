import pymorphy2

morph = pymorphy2.MorphAnalyzer()


def get_word_form(quantity, word):
    word_form = morph.parse(word)[0].make_agree_with_number(quantity).word
    return word_form

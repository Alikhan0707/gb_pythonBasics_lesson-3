def int_func(word):

    word_list = list(word)

    first_letter = word_list.pop(0)

    word_list.insert(0, first_letter.upper())

    new_word = ''

    for i in word_list:

        new_word += i

    return new_word


def sent_func(text):

    sentence_list = text.split()

    new_sentence = ''

    for i in sentence_list:

        new_sentence += int_func(i + ' ')

    return new_sentence

y = input('Enter sentence: ')

print(sent_func(y))



def break_words(stuff):
    words = stuff.split(' ')
    return words

def sort_words(words):
    return sorted(words)
    # do this with words.sorted?
    #yes in theory but it doesn't work in python 3.6

def print_first_word(words):
    word = words[0]
    print(word)

def print_last_word(words):
    word = words[0]
    print(word)

def sort_sentence(sentence):
    #uses other functions to split and sort words in a sentence
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    words = break_words(sentence)
    words = sort_words(words)
    print_first_word(words)
    print_last_word(words)

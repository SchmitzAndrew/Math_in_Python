import random


def create_words():
    possible_words = ["Daft_Punk", "Eric_Andre", "Kraft_Punk", "Aphex_Twin", "Charlie_Brown", "Bill_Watterson "]
    p = random.randrange(-5, 5, ) / 10
    w = [30 + p, 10 + p, 5 + p, 20 + p, 15 + p, 20 + p]

    word_list = random.choices(possible_words, weights = w, k=10000)

    return word_list

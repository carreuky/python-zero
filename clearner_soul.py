words =[ 'touchMe','heroHero', 'Sebsatain', 'touchMe' ,'heroHero', 'yuri alpha', 'Aura']

n =3


def get_n_longest_unique_words(words, n):
    unique_words = get_unique_words(words)
    #soreted give in ascending order, small to big
    #revese=true if the oppose, we want big first
    #key=len sort by the leng of each order
    sorted_words = sorted(unique_words, key=len, reverse=True)
    #slice up to nth word, exluceinf the nth,we want only nth
    #number of words
    return sorted_words[:n]


def get_unique_words(words):
    unique_words = []
    for word in words:
        if words.count(word) == 1:
            unique_words.append(word)

    return unique_words


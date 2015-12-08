import random

def db_get_random_word():
    dictionary={}
    f = open('../db/words.db', 'r')
    for line in f:
        tok=line.split('#')
        dictionary[tok[0]]=tok[1]
    return random.choice(dictionary.items())



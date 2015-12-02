import random

def load_words_from_file():
    dictionary={}
    f = open('parole.db', 'r')
    for line in f:
        tok=line.split('#')
        dictionary[tok[0]]=tok[1]
    #print(dictionary)
    return dictionary

def get_random_word(diz):
    import random
    return random.choice(diz.items())

def game_coontroller_word_definition():
    diz=load_words_from_file()
    item=get_random_word(diz)
    question='Hai 10 secondi per dirmi il significato di: '+item[0]+'\n'
    ans=raw_input(question)
    #send answer and question to another user
    print('Qualcuno sta correggendo la tua risposta, dovrebbe assomigliare a questa:\n'+item[1])
    

game_coontroller_word_definition()

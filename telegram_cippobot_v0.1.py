# -*- coding: utf-8 -*-

import telegram
import time
import requests
import json
import re
import datetime
from bot_functions import *
from Queue import Queue
from threading import Thread

f=open('token.txt','r')
token=f.read()
token=token[:-1]

bot=telegram.Bot(token)
print bot.getMe()

try:
    LAST_UPDATE_ID= bot.getUpdates()[-1].update_id
except IndexError:
    LAST_UPDATE_ID = None
    
messages_queue=Queue()

while True:
    time.sleep(1)
    
    for update in bot.getUpdates(offset=LAST_UPDATE_ID,timeout=10):
        if is_new_chat(update.message):
            messages_queue.put(update.message)
            #crea thread per gestire messaggi di questo nuovo utente
            print 'new thread created, name:'+str(update.message.chat_id)
            if update.message.chat.type==u'private':
                t = Chat_controller(update.message.chat.id, messages_queue, bot)
                t.start()
            else:
                t = Group_controller(update.message.chat.id, messages_queue, bot)
                t.start()
        else:
            messages_queue.put(update.message)
            #aggiunge messaggio alla pila
            print 'new message in queue'       
        LAST_UPDATE_ID = update.update_id+1

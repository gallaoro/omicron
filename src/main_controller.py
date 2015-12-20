# -*- coding: utf-8 -*-

import telegram
import time
import requests
import json
import re
import datetime
from functions import *
from controllers import *
from Queue import Queue
from threading import Thread

f=open('../tokens/telegram-token.txt','r')
token=f.read()
token=token[:-1]

bot=telegram.Bot(token)
print bot.getMe()

try:
    LAST_UPDATE_ID= bot.getUpdates()[-1].update_id
except IndexError:
    LAST_UPDATE_ID = None

messages_queue=Queue()
internal_queue=Queue()

t=Global_dispatcher_controller(internal_queue)
t.start()

while True:
    time.sleep(1)
    
    for update in bot.getUpdates(offset=LAST_UPDATE_ID,timeout=10):
        if is_new_chat(update.message):
            messages_queue.put(update.message)
            #creates thread for single user chat
            print 'new thread created, name:'+str(update.message.chat_id)
            if update.message.chat.type==u'private':
                t = Userchat_controller(update.message.chat.id, messages_queue, bot, internal_queue)
                t.start()
        else:
            messages_queue.put(update.message)      
        LAST_UPDATE_ID = update.update_id+1


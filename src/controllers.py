# -*- coding: utf-8 -*-

from threading import Thread
from db_functions import *
import sys
import time
import datetime
import random

class Userchat_controller(Thread):
    def __init__(self, chat_id, message_queue, bot):
        Thread.__init__(self)
        self.chat_id=chat_id
        self.message_queue=message_queue
        self.bot=bot
    def run(self):
        while True:
            if not self.message_queue.empty():
                message = self.message_queue.get(block=False)
                if not message.chat_id==self.chat_id:
                    self.message_queue.put(message)
                    time.sleep(1)
                else:
                    print 'thread:'+str(self.chat_id)+' has catched message from:'+str(message.chat_id)
                    if 'a' in message.text.lower():
                        question=db_get_random_question()
                        print question
                        self.bot.sendMessage(chat_id=self.chat_id,text=question)
            else:
                time.sleep(1)

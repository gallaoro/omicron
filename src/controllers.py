# -*- coding: utf-8 -*-

from threading import Thread
from db_functions import *
import sys
import time
import datetime
import random

class Userchat_controller(Thread):
    def __init__(self, chat_id, message_queue, bot, internal_queue):
        Thread.__init__(self)
        self.chat_id=chat_id
        self.message_queue=message_queue
        self.bot=bot
        self.is_waiting_for_answer=False
        self.last_answer=''
        self.last_question_id=0
        self.internal_queue=internal_queue
    def run(self):
        while True:
            if not self.message_queue.empty():
                message = self.message_queue.get(block=False)
                if not message.chat_id==self.chat_id:
                    self.message_queue.put(message)
                    time.sleep(1)
                else:
                    print('thread:'+str(self.chat_id)+' has catched message from:'+str(message.chat_id))
                    if self.is_waiting_for_answer:
                        self.last_answer=message.text
                        db_save_answer(self.last_question_id,self.last_answer, self.chat_id)
                        self.is_waiting_for_answer=False
                        self.bot.sendMessage(chat_id=self.chat_id,text='Risposta salvata')
                    elif 'a' in message.text.lower():
                        question=db_get_random_question()
                        self.bot.sendMessage(chat_id=self.chat_id,text=question[1])
                        self.is_waiting_for_answer=True
                        self.last_question_id=question[0]
            else:
                time.sleep(1)
                
                
                
class Global_dispatcher_controller(Thread):
    def __init__(self,internal_queue):
        Thread.__init__(self)
        self.internal_queue=internal_queue
    def run(self):
        while True:
            if not self.internal_queue.empty():
                time.sleep(1)
        

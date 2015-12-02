# -*- coding: utf-8 -*-

from threading import Thread
import sys
import time
import datetime
import random
import pytz

SALUTI=[['ciao'],['eila'],['ei'],['bella'],['salve'],['giorno'],['buongiorno']]
INSULTI=['vaffanculo', 'fanculo', ['vai','in','mona'], 'crepa', 'troia', 'stronzo', ['to','mare']]
USERS=[]

def is_new_chat(message):
    try:
        message_id=message.message_id
        from_user=message.from_user
        date=message.date
        chat=message.chat
        
        new_group=message.group_chat_created
        
        type_of_chat= message.chat.type
        
        if new_group:
            return True
        elif type_of_chat==u'private':
            if from_user.id not in USERS:
                USERS.append(from_user.id)
                return True
            else:
                return False
        else:
            if message.chat.id not in USERS:
                USERS.append(message.chat.id)
                return True
            else:
                return False
    except ValueError:
        print "Not a telegram.Message"

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

class Chat_controller(Thread):
    def __init__(self, chat_id, queue, bot):
        Thread.__init__(self)
        self.chat_id=chat_id
        self.queue=queue
        self.bot=bot
        self.time
    def run(self):
        while True:
            if not self.queue.empty():
                message = self.queue.get(block=False)
                if not message.chat_id==self.chat_id:
                    self.queue.put(message)
                    time.sleep(1)
                else:
                    print str(self.chat_id)+': message catch'
                    if 'Ciao' in message.text:
                        self.bot.sendMessage(chat_id=self.chat_id, text='Ciao')
                        self.bot.sendMessage(chat_id=self.chat_id, text=str(message))
                    if 'parola' in message.text.lower():
                        diz=load_words_from_file()
                        item=get_random_word(diz)
                        question='Hai 10 secondi per dirmi il significato di: '+item[0]+'\n'
                                        
            else:
                time.sleep(1)
            

class Group_controller(Thread):
    def __init__(self, chat_id, queue, bot):
        Thread.__init__(self)
        self.ita_timezone=pytz.timezone('Europe/Rome')
        self.chat_id=chat_id
        self.queue=queue
        self.bot=bot
        self.morning_alarm=(7,0)
        self.goodmorning_sent=True
        self.morning_alarm_enabled=True
        self.day=datetime.datetime.now(self.ita_timezone).day
    def run(self):
        while True:
            if not self.day==datetime.datetime.now(self.ita_timezone).day:
                if self.morning_alarm_enabled:
                    self.goodmorning_sent=False
                    self.day=datetime.datetime.now(self.ita_timezone).day
        
            if self.goodmorning_sent==False and datetime.datetime.now(self.ita_timezone).hour>=self.morning_alarm[0] and datetime.datetime.now(self.ita_timezone).minute>=self.morning_alarm[1]:
                self.bot.sendMessage(chat_id=self.chat_id, text=goodmorning())
                self.goodmorning_sent=True
                
            if not self.queue.empty():
                message = self.queue.get(block=False)
                if not message.chat_id==self.chat_id:
                    self.queue.put(message)
                    time.sleep(1)
                else:
                    print str(self.chat_id)+': message catch'
                    if 'ciao' in message.text.lower():
                        self.bot.sendMessage(chat_id=self.chat_id, text='Ciao')
                    if goodmorning_change_recognize(message.text.lower()):
                        self.morning_alarm = goodmorning_change(message.text.lower())
                        if self.morning_alarm[1]<10:
                            self.bot.sendMessage(chat_id=self.chat_id, text='Sveglia impostata alle: '+str(self.morning_alarm[0])+':0'+str(self.morning_alarm[1]))
                        else:
                            self.bot.sendMessage(chat_id=self.chat_id, text='Sveglia impostata alle: '+str(self.morning_alarm[0])+':'+str(self.morning_alarm[1]))
                            
                    #debug code
                    if 'lalunanera' in message.text.lower():
                        self.goodmorning_sent=False
                        self.bot.sendMessage(chat_id=self.chat_id, text=str(datetime.datetime.now(self.ita_timezone)))
                    
                    
                sys.stdout.flush()
            else:
                time.sleep(1)

def goodmorning():
    n=random.randint(0,6)
    
    now=datetime.datetime.now(pytz.timezone('Europe/Rome'))

    if now.minute<10:
        minutes='0'+str(now.minute)
    else:
        minutes=str(now.minute)
    
    if n==0:
        return 'Sono le '+str(now.hour)+':'+minutes+' e tutto va bene\n #semicit'
    elif n==1:
        return 'Buongiorno gente'
    elif n==2:
        return 'Giorno'
    elif n==3:
        return u'Auf che l\'è morghen'
    elif n==4:
        return 'Ore '+str(now.hour)+':'+minutes+', sveglia!'
    elif n==5:
        return 'Svegliaaaaa'
    elif n==6:
        return 'Sveglia gentaglia'   
    return 'Buongiorno'

def goodmorning_change_recognize(text):
    tokenized=text.split()
    if '/buongiorno' in tokenized:
        return True
    else:
        return False

def goodmorning_change(text):
    tokenized=text.split()
    if '/buongiorno' in tokenized:
        tokenized.remove('/buongiorno')
        if len(tokenized)>0:
            try:
                n=int(tokenized[0])
                if n>0 and n<24:
                    return n, 0
            except ValueError:
                try:
                    tokenized1=tokenized[0].split(':')
                    if int(tokenized1[0])>=0 and int(tokenized1[0])<24:
                        if int(tokenized1[1])>=0 and int(tokenized1[1])<60:
                            return int(tokenized1[0]), int(tokenized1[1])
                        else:
                            return 7,0
                    else:
                        return 7,0
                except ValueError:
                    return 7,0
        return 7,0













def riconosci_saluto(text):
    if type(text)==type([]):
        n=len(text)
        for i in range(len(text)):
            text[i]=text[i].lower()
        if n>0:
            if text in SALUTI:
                return text
                

def riconosci_insulto(text):
    if type(text)==type([]):
        n=len(text)
        for i in range(len(text)):
            text[i]=text[i].lower()
        if n>0:
            if text in INSULTI:
                return text
                

def get_weather_forecasts(location):
    current_date=time.time()
    r=requests.get('http://api.openweathermap.org/data/2.5/forecast?q='+str(location)+'&appid=bd82977b86bf27fb59a04b61b657fb6f')
    j=json.loads(r.text)
    next_forecast=j['list'][0]
    if next_forecast['dt']<current_date:
        next_forecast=j['list'][1]
    ora=datetime.datetime.fromtimestamp(next_forecast['dt'])
    ora=ora.strftime('%H:%M')
    output='Alle '+str(ora)+':\n'+get_printable_weather(next_forecast['weather'][0],location)
    
    r=requests.get('http://api.openweathermap.org/data/2.5/forecast/daily?q='+str(location)+'&appid=bd82977b86bf27fb59a04b61b657fb6f')
    j=json.loads(r.text)
    next_forecast=j['list'][0]
    if next_forecast['dt']<current_date:
        next_forecast=j['list'][1]
    output=output+'\nDomani alle 12:00:\n'+get_printable_weather(next_forecast['weather'][0],location)
    
    return output
    
    
def get_printable_weather(weather, location):
    if location==None or location=='':
        location=u'Levico Terme'
    emo=telegram.Emoji.SUN_BEHIND_CLOUD
    if weather['id']==800:
        emo=telegram.Emoji.BLACK_SUN_WITH_RAYS
    if weather['id']>=801 and weather['id']<=804:
        emo=telegram.Emoji.CLOUD
    if weather['id']>=600 and weather['id']<=622:
        emo=telegram.Emoji.SNOWFLAKE
    if weather['id']>=500 and weather['id']<=531:
        emo=telegram.Emoji.UMBRELLA_WITH_RAIN_DROPS
    if weather['id']>=200 and weather['id']<=232:
        emo=telegram.Emoji.HIGH_VOLTAGE_SIGN
    return u'Il meteo a '+location+u': '+emo.decode('utf-8')+u'\n'+weather['main']+u': '+weather['description']
    
    
def riconosci_comando(list1):
    if len(list1)>0:
        if list1[0][0]=='/':
            return True
        else:
            return False
            
def riconosci_meteo(list1):
    localita=False
    if len(list1)>1:
        if list1[0]=='/meteo':
       	    list1.remove('/meteo')
       	    localita=''
       	    for i in list1:
       	        localita+=i+' '
       	    if localita=='':
       	        localita=False
    return localita

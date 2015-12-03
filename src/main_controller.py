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

f=open('../tokens/telegram-token.txt','r')
token=f.read()
token=token[:-1]

bot=telegram.Bot(token)
print bot.getMe()

try:
    LAST_UPDATE_ID= bot.getUpdates()[-1].update_id
except IndexError:
    LAST_UPDATE_ID = None


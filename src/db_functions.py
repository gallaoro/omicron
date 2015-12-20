#!/usr/bin/python
import MySQLdb
import random


def db_init():
    db = MySQLdb.connect(host="localhost", user="root", passwd="", db="omicron")
    # setup a cursor object using cursor() method
    cursor = db.cursor()

    cursor.execute("SET NAMES utf8;") #or utf8 or any other charset you want to handle

    cursor.execute("SET CHARACTER SET utf8;") #same as above

    cursor.execute("SET character_set_connection=utf8;") #same as above
    return cursor


def db_get_random_question():
    cur=db_init()

    cur.execute('SELECT * FROM QUESTIONS')
    
    return random.choice(cur.fetchall())


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
    return cursor, db


def db_get_random_question():
    db=db_init()    
    cur=db[0]
    db=db[1]

    cur.execute('SELECT * FROM QUESTIONS')
    result=cur.fetchall()
    
    cur.close()
    db.close()    
    
    return random.choice(result)

def db_save_answer(id_question, answer_text):
    db=db_init()    
    cur=db[0]
    db=db[1]
    
    cur.execute('INSERT INTO ANSWERS (id_question, answer_text) VALUES('+str(id_question)+',\''+answer_text+'\')')
    db.commit()
    
    cur.close()
    db.close()


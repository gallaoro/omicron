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

def db_save_answer(id_question, answer_text, id_telegram):
    db=db_init()    
    cur=db[0]
    db=db[1]
    
    answer_text=answer_text.replace('"','""') #so you can insert quoted strings
    
    cur.execute("INSERT INTO ANSWERS (id_question, answer_text, id_telegram) VALUES("+str(id_question)+",\""+answer_text+"\","+str(id_telegram)+")")
    db.commit()
    
    cur.close()
    db.close()

def db_is_new_user(id_telegram):
    db=db_init()    
    cur=db[0]
    db=db[1]
    
    cur.execute('SELECT * FROM USERS WHERE id_telegram='+str(id_telegram))
    
    result=cur.fetchone()
    
    cur.close()
    db.close()
    
    if result==None:
        return True
    else:
        return False
        
def db_insert_new_user(id_telegram, user_name):
    db=db_init()    
    cur=db[0]
    db=db[1]
    
    user_name=user_name.replace('"','""') #so you can insert quoted strings
    
    cur.execute("INSERT INTO USERS (id_telegram, name) VALUES("+str(id_telegram)+",\""+user_name+"\")")
    db.commit()
    
    cur.close()
    db.close()
    


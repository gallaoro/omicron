DROP DATABASE IF EXISTS omicron;
CREATE DATABASE IF NOT EXISTS omicron;

USE omicron
/* Create USERS table */
CREATE TABLE USERS(id_user INTEGER PRIMARY KEY,
name TEXT);


CREATE TABLE QUESTIONS(id_question INTEGER PRIMARY KEY,
question_text TEXT CHARACTER SET utf8);

CREATE TABLE ANSWERS(id_answer INTEGER PRIMARY KEY,
id_question INTEGER,
answer_text TEXT);

CREATE TABLE CORRECTIONS(id_correction INTEGER PRIMARY KEY,
id_question INTEGER,
id_answer INTEGER,
correction_text TEXT);

/* Create few records */
INSERT INTO USERS VALUES(1,'Gabriele');
INSERT INTO USERS VALUES(2,'Marta');
INSERT INTO USERS VALUES(3,'Tommaso');
INSERT INTO USERS VALUES(4,'Silvia');
INSERT INTO USERS VALUES(5,'Roberto');

INSERT INTO QUESTIONS VALUES(1,'Quale è il significato di barile?');
INSERT INTO QUESTIONS VALUES(2,'Dove sono se sto vedendo "il pirellone"?');
INSERT INTO QUESTIONS VALUES(3,'Che creatura mitologica aveva il corpo di un leone e la testa e le ali di un\'acquila?');
INSERT INTO QUESTIONS VALUES(4,'Pesa di più una mole d\'ossigeno o una di idrogeno?');
INSERT INTO QUESTIONS VALUES(5,'Quale è il gerundio presente di essere?');

/* Display all the records from the table */
SELECT * FROM USERS;

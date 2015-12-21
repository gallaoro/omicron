DROP DATABASE IF EXISTS omicron;
CREATE DATABASE IF NOT EXISTS omicron;

USE omicron
/* Create USERS table */
CREATE TABLE USERS(id_user INTEGER PRIMARY KEY AUTO_INCREMENT,
name TEXT CHARACTER SET utf8,
telegram_id INTEGER);

CREATE TABLE QUESTIONS(id_question INTEGER PRIMARY KEY AUTO_INCREMENT,
question_text TEXT CHARACTER SET utf8);

CREATE TABLE ANSWERS(id_answer INTEGER PRIMARY KEY AUTO_INCREMENT,
id_question INTEGER,
answer_text TEXT CHARACTER SET utf8);

CREATE TABLE CORRECTIONS(id_correction INTEGER PRIMARY KEY AUTO_INCREMENT,
id_question INTEGER,
id_answer INTEGER,
correction_text TEXT CHARACTER SET utf8);

/* Create few records */
INSERT INTO USERS (name) VALUES('Gabriele'),('Marta'),('Tommaso'),('Silvia'),('Roberto');

INSERT INTO QUESTIONS (question_text) VALUES('Quale è il significato di barile?'),
('Dove sono se sto vedendo "il pirellone"?'),
('Che creatura mitologica ha il corpo di un leone e la testa e le ali di un\'acquila?'),
('Pesa di più una mole d\'ossigeno o una di idrogeno?'),
('Quale è il gerundio presente di essere?');



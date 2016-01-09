# omicron

Porpouse
---------
Create a telegram bot which periodically sends to users questions about grammar

To do
-----
* ~~Create a user-thread which retrieve a question from db and sends to the user~~
* Create a controller which given a question and an answer asks to a user if it's correct

Tasks
-------
### main_controller:
* Controls messages from users
** If finds a message from a new user creates a thread to manage the chat with that user end inserts the messages in the *telegram_messages_queue*
** If finds a message from a known user just inserts the message in the *telegram_messages_queue*

###user_thread:
* Controls the *telegram_messages_queue* for messages for himself
* Access the db to choose a question and send to the user
* Waits for an answer to the given question and saves in the db

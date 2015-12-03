# omicron

Obiettivo
---------
Creare un bot telegram che periodicamente invii agli utenti delle domande su grammatica e affini

To do
-----
* Realizzare uno user_thread che prelevi una domanda da db e la invii all'utente
* Inserire nel main_controller la ricerca nel db di una risposta 
* 

Compiti
-------
### main_controller:
* Controlla messaggi provenienti da utenti telegram
* Se trova un messaggio di un nuovo utente crea un thread per gestire la chat con quell'utente e inserisce il messaggio nella telegram_messages_queue
* Se trova un messaggio di un utente già conosciuto inserisce il messaggio nella coda telegram_messages_queue  
* Prende una risposta da db e la trasforma in una messaggio interno per alcuni thread

###user_thread:
* Controlla la coda telegram_messages_queue per messaggi per se stesso
* Accede al db per scegliere una domanda e inviarla all'utente
* Aspetta una risposta alla domanda fatta e la inserisce ne db
* Controlla la internal_messages_queue per messaggi da inoltrare nella chat(risposte da correggere)


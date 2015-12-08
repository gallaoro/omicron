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

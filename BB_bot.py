# -*- coding: utf-8 -*-
import logging as log
from BB_config import dsn_hostname, dsn_uid, dsn_pwd, dsn_driver, dsn_database, dsn_port, dsn_protocol, TOKEN
import ibm_db

import telebot

bot = telebot.TeleBot(TOKEN)

log.basicConfig(filename='C:\\Users\EKAU.STARSPB\Desktop\Bot\Bot_log.log',level=log.INFO, format='%(asctime)s %(message)s', datefmt='%m.%d.%Y %H:%M:%S')

hi_list=[]
hi_list=['hi','hello','привет','здравствуй','здравствуйте','приветик']

#{'content_type': 'text', 'message_id': 108, 'from_user': {'id': 591342003, 'is_bot': False, 'first_name': 'Kathy', 'username': 'NoWord', 'last_name': None, 'language_code': 'ru', 'can_join_groups': None, 'can_read_all_group_messages': None, 'supports_inline_queries': None}, 'date': 1599125237, 'chat': {'id': 591342003, 'type': 'private', 'title': None, 'username': 'NoWord', 'first_name': 'Kathy', 'last_name': None, 'all_members_are_administrators': None, 'photo': None, 'description': None, 'invite_link': None, 'pinned_message': None, 'permissions': None, 'slow_mode_delay': None, 'sticker_set_name': None, 'can_set_sticker_set': None}, 'forward_from': None, 'forward_from_chat': None, 'forward_from_message_id': None, 'forward_signature': None, 'forward_date': None, 'reply_to_message': None, 'edit_date': None, 'media_group_id': None, 'author_signature': None, 'text': 'Hi', 'entities': None, 'caption_entities': None, 'audio': None, 'document': None, 'photo': None, 'sticker': None, 'video': None, 'video_note': None, 'voice': None, 'caption': None, 'contact': None, 'location': None, 'venue': None, 'animation': None, 'dice': None, 'new_chat_member': None, 'new_chat_members': None, 'left_chat_member': None, 'new_chat_title': None, 'new_chat_photo': None, 'delete_chat_photo': None, 'group_chat_created': None, 'supergroup_chat_created': None, 'channel_chat_created': None, 'migrate_to_chat_id': None, 'migrate_from_chat_id': None, 'pinned_message': None, 'invoice': None, 'successful_payment': None, 'connected_website': None, 'json': {'message_id': 108, 'from': {'id': 591342003, 'is_bot': False, 'first_name': 'Kathy', 'username': 'NoWord', 'language_code': 'ru'}, 'chat': {'id': 591342003, 'first_name': 'Kathy', 'username': 'NoWord', 'type': 'private'}, 'date': 1599125237, 'text': 'Hi'}}


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    log.info(
            'Incoming message: '+ str(message.text) + ' from: ID '+ str(message.from_user.id) +
            ' ' + str(message.from_user.first_name) + ' @' + str(message.from_user.username ))
    mess=""
    mess = message.text.lower()
    if mess in hi_list:
        print('User wrote: ',message.text)
        bot.send_message(message.from_user.id,"Здравствуйте, {}!".format(message.chat.first_name))

    elif message.text=='/help':
        bot.send_message(message.from_user.id,
                        "Напишите язык, например, FRA, чтобы получить список тех, кто им владеет")
        bot.send_message(message.from_user.id,
                        "Напишите языковую пару, например, Rus-deu, чтобы получить список работающих с ней переводчиков")
        bot.send_message(message.from_user.id,
                        "Напишите мне фамилию переводчика, чтобы узнать о нем побольше")
        bot.send_message(message.from_user.id,
                        "Напишите /lang, чтобы получить список языков")
        print('User asked me for help')

    elif message.text in Tra_list: #Move out into a sep function
        dsn='DRIVER={IBM DB2 ODBC DRIVER};DATABASE=BLUDB;HOSTNAME=dashdb-txn-sbox-yp-lon02-15.services.eu-gb.bluemix.net;PORT=50000;PROTOCOL=TCPIP;UID=xxr30091;PWD=t6ngb3lrd+s6f22q;'
        import ibm_db
        try:
            conn = ibm_db.connect(dsn, "", "")
            print ("Connected to database")
            #bot.send_message(message.from_user.id,"Database connection established")
        except:
            print ("Unable to connect: ", ibm_db.conn_errormsg() )
            bot.send_message(message.from_user.id,"Sorry, the database seems to be unavailable")

        selectQuery = "select * from TRANSLATORS where L_NAME like '%"+message.text+"%'"

        selectStmt2 = ibm_db.exec_immediate(conn, selectQuery)

        while ibm_db.fetch_row(selectStmt2) != False:
            print (
            " TYPE: ",  ibm_db.result(selectStmt2, 0), " Last name: ",
              ibm_db.result(selectStmt2, "L_NAME"),
               'First_name: ', ibm_db.result(selectStmt2, "F_NAME", )
               )

            bot.send_message(
            message.from_user.id, str(ibm_db.result(selectStmt2, 0))+' '+str(ibm_db.result(selectStmt2, 1))+
            ' '+str(ibm_db.result(selectStmt2,2))+' \n'+str(ibm_db.result(selectStmt2,3))+
            '\n'+str(ibm_db.result(selectStmt2,4))+'\n '+str(ibm_db.result(selectStmt2,5))
                    )
    elif mess in allLanguages.keys(): #Move out into a sep function
        dsn='DRIVER={IBM DB2 ODBC DRIVER};DATABASE=BLUDB;HOSTNAME=dashdb-txn-sbox-yp-lon02-15.services.eu-gb.bluemix.net;PORT=50000;PROTOCOL=TCPIP;UID=xxr30091;PWD=t6ngb3lrd+s6f22q;'
        import ibm_db
        try:
            conn = ibm_db.connect(dsn, "", "")
            print ("Connected to database")
            #bot.send_message(message.from_user.id,"Database connection established")
        except:
            print ("Unable to connect: ", ibm_db.conn_errormsg() )
            bot.send_message(message.from_user.id,"Sorry, the database seems to be unavailable")

        selectQuery = "select * from TRANSLATORS where LANG like '%"+mess.upper()+"%'"

        selectStmt2 = ibm_db.exec_immediate(conn, selectQuery)
        while ibm_db.fetch_row(selectStmt2) != False:
            print (
                    " TYPE: ",  ibm_db.result(selectStmt2, 0),
                     " Last name: ",  ibm_db.result(selectStmt2, "L_NAME"),
                      'First_name: ', ibm_db.result(selectStmt2, "F_NAME", )
                    )
            bot.send_message(
            message.from_user.id, str(ibm_db.result(selectStmt2,0))+' '+str(ibm_db.result(selectStmt2,1))+
            ' '+str(ibm_db.result(selectStmt2,2))+' \n'+str(ibm_db.result(selectStmt2,3))+' \n'+str(ibm_db.result(selectStmt2,4))+
            '\n'+str(ibm_db.result(selectStmt2,5))
            )
    elif len(message.text)==7 and mess[:3] in allLanguages.keys(): #Move out into a sep function
        dsn='DRIVER={IBM DB2 ODBC DRIVER};DATABASE=BLUDB;HOSTNAME=dashdb-txn-sbox-yp-lon02-15.services.eu-gb.bluemix.net;PORT=50000;PROTOCOL=TCPIP;UID=xxr30091;PWD=t6ngb3lrd+s6f22q;'
        import ibm_db
        try:
            conn = ibm_db.connect(dsn, "", "")
            print ("Connected to database")
            #bot.send_message(message.from_user.id,"Database connection established")
        except:
            print ("Unable to connect: ", ibm_db.conn_errormsg() )
            bot.send_message(message.from_user.id,"Sorry, the database seems to be unavailable")

        selectQuery = "select * from TRANSLATORS where LANG like '%"+mess.upper()+"%'"

        selectStmt2 = ibm_db.exec_immediate(conn, selectQuery)
        while ibm_db.fetch_row(selectStmt2) != False:
            print (
                    " TYPE: ",  ibm_db.result(selectStmt2, 0),
                     " Last name: ",  ibm_db.result(selectStmt2, "L_NAME"),
                      'First_name: ', ibm_db.result(selectStmt2, "F_NAME", )
                    )
            bot.send_message(
            message.from_user.id, str(ibm_db.result(selectStmt2,0))+' '+str(ibm_db.result(selectStmt2,1))+
            ' '+str(ibm_db.result(selectStmt2,2))+' \n'+str(ibm_db.result(selectStmt2,3))+' \n'+str(ibm_db.result(selectStmt2,4))+
            '\n'+str(ibm_db.result(selectStmt2,5)))

    elif message.text=='/lang':
        for item in allLanguages:
            code=str(item)
            code=code.upper()
            response=''
            response=allLanguages[item]+': '+code
            bot.send_message(message.from_user.id,response)

    else:
        bot.send_message(message.from_user.id,'Извините {}! \n я не понял'.format(message.chat.first_name))
        bot.send_message(message.from_user.id,'Может быть, вы нажмете на /help ?')
        print('User wrote: ',message.text)


bot.polling(none_stop=True,interval=0)
# -*- coding: utf-8 -*-
import logging as log
from BB_config import dsn_hostname, dsn_uid, dsn_pwd, dsn_driver, dsn_database, dsn_port, dsn_protocol, TOKEN
import ibm_db

import telebot

bot = telebot.TeleBot(TOKEN)

TABLENAME="BB_table" #"XXR30091.BB_TABLE"
#my id = 591342003

log.basicConfig(filename='C:\\Users\EKAU.STARSPB\Desktop\BolnichkaBot\BB_log.log',level=log.INFO, format='%(asctime)s %(message)s', datefmt='%m.%d.%Y %H:%M:%S')

dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd)

hi_list=['hi','hello','привет','здравствуй','здравствуйте','приветик']

#{'content_type': 'text', 'message_id': 108, 'from_user': {'id': 591342003, 'is_bot': False, 'first_name': 'Kathy', 'username': 'NoWord', 'last_name': None, 'language_code': 'ru', 'can_join_groups': None, 'can_read_all_group_messages': None, 'supports_inline_queries': None}, 'date': 1599125237, 'chat': {'id': 591342003, 'type': 'private', 'title': None, 'username': 'NoWord', 'first_name': 'Kathy', 'last_name': None, 'all_members_are_administrators': None, 'photo': None, 'description': None, 'invite_link': None, 'pinned_message': None, 'permissions': None, 'slow_mode_delay': None, 'sticker_set_name': None, 'can_set_sticker_set': None}, 'forward_from': None, 'forward_from_chat': None, 'forward_from_message_id': None, 'forward_signature': None, 'forward_date': None, 'reply_to_message': None, 'edit_date': None, 'media_group_id': None, 'author_signature': None, 'text': 'Hi', 'entities': None, 'caption_entities': None, 'audio': None, 'document': None, 'photo': None, 'sticker': None, 'video': None, 'video_note': None, 'voice': None, 'caption': None, 'contact': None, 'location': None, 'venue': None, 'animation': None, 'dice': None, 'new_chat_member': None, 'new_chat_members': None, 'left_chat_member': None, 'new_chat_title': None, 'new_chat_photo': None, 'delete_chat_photo': None, 'group_chat_created': None, 'supergroup_chat_created': None, 'channel_chat_created': None, 'migrate_to_chat_id': None, 'migrate_from_chat_id': None, 'pinned_message': None, 'invoice': None, 'successful_payment': None, 'connected_website': None, 'json': {'message_id': 108, 'from': {'id': 591342003, 'is_bot': False, 'first_name': 'Kathy', 'username': 'NoWord', 'language_code': 'ru'}, 'chat': {'id': 591342003, 'first_name': 'Kathy', 'username': 'NoWord', 'type': 'private'}, 'date': 1599125237, 'text': 'Hi'}}


@bot.message_handler(commands=['start'])
def Start_handler(message):
    log.info(
            'Incoming message: '+ str(message.text) + ' from: ID '+ str(message.from_user.id) +
            ' ' + str(message.from_user.first_name) + ' @' + str(message.from_user.username ))

    bot.send_message(message.from_user.id,'Здравствуйте, {}! \n Вы нажали /start'.format(message.chat.first_name))
    print('User {} pressed "/Start" '.format(message.chat.first_name))


@bot.message_handler(commands=['help'])
def Help_handler(message):
    SadEmoji = u'\U0001F623'
    bot.send_message(message.from_user.id,
                    "Буду рад вам помочь, но пока не умею, извините "+SadEmoji)
    HurricaneEmoji = u'\U0001F300'#works as model

    #bot.send_message(message.from_user.id,SadEmoji)
    print('User {} asked me for help'.format(message.chat.first_name))


@bot.message_handler(commands=['add'])
def Add_handler(message):

    user_id=str(message.from_user.id)
    username=str(message.from_user.username)
    user_firstname=str(message.from_user.first_name)

    log.info(
            'Incoming message: '+ str(message.text) + ' from: ID '+ user_id +
            ' ' + user_firstname + ' @' + username)

    conn = ibm_db.connect(dsn, "", "")
    print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)



    insertQuery = "insert into "+TABLENAME+" values ('"+user_id+"','"+username+"','"+user_firstname+"','','')"
    try:
        insertStmt = ibm_db.exec_immediate(conn, insertQuery)
        bot.send_message(message.from_user.id,'Отлично, {}! \n Вы успешно добавлены в базу'.format(message.chat.first_name))
        print ("Data inserted: User ",user_id,username,user_firstname)
        log.info("Data inserted: User "+user_id+' @'+username+' '+user_firstname)

    except:
        bot.send_message(message.from_user.id,'Вас не удалось добавить в базу. \n Возможно, вы в ней уже есть.')
        print ("Data insertion failed: User ",user_id,' @',username,user_firstname)
        log.info("Data insertion failed: User "+user_id+' @'+username+' '+user_firstname)

    ibm_db.close(conn)
    print('User {} tried to add his name into the DB and failed'.format(user_firstname))



@bot.message_handler(commands=['help'])
def Help_handler(message):
    SadEmoji = u'\U0001F623'
    bot.send_message(message.from_user.id,
                    "Буду рад вам помочь, но пока не умею, извините "+SadEmoji)
    HurricaneEmoji = u'\U0001F300'#works as model

    #bot.send_message(message.from_user.id,SadEmoji)
    print('User asked me for help')



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


    else:
        bot.send_message(message.from_user.id,'Извините, {}! \n Я вас не понял'.format(message.chat.first_name))
        bot.send_message(message.from_user.id,'Может быть, вы нажмете на /help ?')
        print('User wrote: ',message.text)


bot.polling(none_stop=True,interval=0)
# -*- coding: utf-8 -*-
import logging as log
from BB_config import dsn_hostname, dsn_uid, dsn_pwd, dsn_driver,\
                      dsn_database, dsn_port, dsn_protocol, TOKEN,\
                      Logpath, TABLENAME
import ibm_db
import telebot
from telebot import types
import time


"""
Работающая версия с описанием команд
кнопками спрашивает, разослать ли
рассылает всем

ЗАДАЧА:
    дать обратную связь с юзером
"""

bot = telebot.TeleBot(TOKEN)

log.basicConfig(filename=Logpath,level=log.INFO, format='%(asctime)s %(message)s', datefmt='%m.%d.%Y %H:%M:%S')

dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd)




@bot.message_handler(commands=['start'])
def Start_handler(message):
    log.info(
            '\n Incoming message: '+ str(message.text) + ' from: ID '+ str(message.from_user.id) +
            ' ' + str(message.from_user.first_name) + ' @' + str(message.from_user.username ))

    bot.send_message(message.from_user.id,'Здравствуйте, {}!\nВас приветствует бот для оповещения волонтеров Больнички'.format(message.chat.first_name))
    bot.send_message(message.from_user.id,"Напишите любое сообщение, и вам будет предложено разослать его волонтерам")
    bot.send_message(message.from_user.id,"Напишите /add, чтобы внести себя в список волонтеров, получающих сообщения")
    bot.send_message(message.from_user.id,"Не забудьте удалить себя из списка командой /delete, когда передумаете их получать")
    bot.send_message(message.from_user.id,"Напишите /help, чтобы получить список доступных команд")

    print('User {} pressed "/Start" '.format(message.chat.first_name))


@bot.message_handler(commands=['help'])
def Help_handler(message):
    bot.send_message(message.from_user.id,"Чтобы внести себя в список рассылки, напишите /add")
    bot.send_message(message.from_user.id,"Чтобы удалить свое имя из списка рассылки, нажмите /delete")
    bot.send_message(message.from_user.id,"Чтобы связаться с админом бота, напишите /admin")

    print('User {} asked me for help'.format(message.chat.first_name))


@bot.message_handler(commands=['add'])
def Add_handler(message):

    user_id=str(message.from_user.id)
    username=str(message.from_user.username)
    user_firstname=str(message.from_user.first_name)

    print('User {} tries to add his name into the DB'.format(user_firstname))
    log.info(
            'User tries to add his name into the DB: '+ str(message.text) + 'ID '+ user_id +
            ' @' + username + ' '+ user_firstname)

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


@bot.message_handler(commands=['admin'])
def admin_handler(message):
    bot.send_message(message.from_user.id,"Админ здесь: @NoWord")

@bot.message_handler(commands=['delete'])
def delete_handler(message):

    user_id=str(message.from_user.id)
    username=str(message.from_user.username)
    user_firstname=str(message.from_user.first_name)

    print('User {} tries to withdraw his name from the DB'.format(user_firstname))
    log.info(
            'User tries to withdraw his name from the DB: '+ str(message.text) + 'ID '+ user_id +
            ' @' + username + ' '+ user_firstname)

    conn = ibm_db.connect(dsn, "", "")
    print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)


    DeleteQuery = "delete from "+TABLENAME+" WHERE id="+user_id
    try:
        DeleteStmt = ibm_db.exec_immediate(conn, DeleteQuery)
        bot.send_message(message.from_user.id,'Вы удалили свое имя из списка. \n Уведомления больше не будут вам присылаться.'.format(message.chat.first_name))
        print ("Data deleted: User ",user_id,username,user_firstname)
        log.info("Data deleted: User "+user_id+' @'+username+' '+user_firstname)

    except:
        bot.send_message(message.from_user.id,'Удаления не получилось. \n Вы точно были в базе?')
        print ("Data withdrawal failed: User ",user_id,' @',username,user_firstname)
        log.info("Data withdrawal failed: User "+user_id+' @'+username+' '+user_firstname)

    ibm_db.close(conn)



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    log.info('\n_ _ _ _ _ _ _ _ _ _ _ _ _ INCOMING MESSAGE _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')
    log.info(
            'Incoming message: '+ str(message.text) + ' from: ID '+ str(message.from_user.id) +
            ' ' + str(message.from_user.first_name) + ' @' + str(message.from_user.username ))

    print("INCOMING MESSAGE "+ str(message.text) + ' from: ID '+ str(message.from_user.id) +
            ' ' + str(message.from_user.first_name) + ' @' + str(message.from_user.username ))

    #mess=""
    global mess;
    mess = message.text
    global author_id;
    author_id = message.from_user.id
    global username;
    username = str(message.from_user.username )


    #Buttons
    keyboard=types.InlineKeyboardMarkup();
    key_yes=types.InlineKeyboardButton(text="Да",callback_data='yes');
    key_no=types.InlineKeyboardButton(text="Нет",callback_data='no');
    keyboard.add(key_yes,key_no)


    Confirm='Разослать это сообщение волонтерам Больнички?'
    bot.send_message(message.from_user.id,text=Confirm, reply_markup=keyboard)

    @bot.callback_query_handler(func=lambda call: True)
    def callback_worker(call):

        if call.data=='yes':


            try:
                i=0
                conn = ibm_db.connect(dsn, "", "")
                print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)
                bot.send_message(author_id,"Рассылаю...")

                #Select all
                selectQuery = "select * from "+TABLENAME
                selectStmt = ibm_db.exec_immediate(conn, selectQuery)

                while ibm_db.fetch_row(selectStmt) != False:
                    print ("Sent to: ID:",  ibm_db.result(selectStmt, 0), " @username:",  ibm_db.result(selectStmt, "USERNAME"))
                    bot.send_message(ibm_db.result(selectStmt, 0),mess)
                    i+=1

                bot.send_message(author_id,"Пользователей, получивших ваше оповещение: {} ".format(i))
                log.info('Разослано пользователям: '+str(i))


            except:
                print ("Unable to connect: ", ibm_db.conn_errormsg())

            ibm_db.close(conn)
            print ("Connection closed")

        else:
            bot.send_message(author_id,"Хорошо, не буду")


def start_working():
    try:
        bot.polling(none_stop=True,interval=0)
    except:
        time.sleep(10)
        start_working()


start_working()
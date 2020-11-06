"""THIS IS GENERAL VERSION
"""

from config import dsn_hostname, dsn_uid, dsn_pwd, dsn_driver, dsn_database, dsn_port, dsn_protocol
import ibm_db


#To be inserted before every start!
TABLENAME="BB_table"

#DB credentials, stored in config file
dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd)

try:
    conn = ibm_db.connect(dsn, "", "")
    print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)

#!!! СЮДА ВПИСАТЬ НЕБОЛЬШОЙ СЕЛЕКТ, А ЛУЧШЕ ИНФУ О ТАБЛИЦЕ - ВИДЕТЬ ТИП ДАННЫХ И КОЛОНКИ
#'''(id varchar(10) PRIMARY KEY NOT NULL, username VARCHAR (30), name varchar(30), Col3 varchar(30), Col4 varchar(30))"'''
#'''from_user': {'id': 591342003, 'is_bot': False, 'first_name': 'Kathy', 'username': 'NoWord' '''

    #One row of data:
    insertQuery = "insert into "+TABLENAME+" values ('591342066','Fiction','Kathy','','')"
    insertStmt = ibm_db.exec_immediate(conn, insertQuery)

    #Few rows:
    ##insertQuery2 = "insert into "+TABLENAME+" values (2, 'Raul', 'Chong', 'Markham','SA'), \
    ##                                                (3, 'Hima', 'Vasudevan', 'Chicago','US')"
    ##
    ##insertStmt2 = ibm_db.exec_immediate(conn, insertQuery2)

except:
    print ("something gone wrong, but I don't know what exactly ", ibm_db.conn_errormsg() )

ibm_db.close(conn)
print ("Connection closed")
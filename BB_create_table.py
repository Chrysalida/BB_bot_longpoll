"""
Just a .py file for manipulating the table remotely: creating a table
"""


from config import dsn_hostname, dsn_uid, dsn_pwd, dsn_driver, dsn_database, dsn_port, dsn_protocol, TABLENAME
import ibm_db


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

    #Dropping first in case the table already exists
    dropQuery = "drop table " + TABLENAME
    dropStmt = ibm_db.exec_immediate(conn, dropQuery)

    #Configure the Create Table DDL statement for your needs!
    createQuery = "create table "+TABLENAME+" (id varchar(10) PRIMARY KEY NOT NULL, \
                                               username VARCHAR (30), \
                                               name varchar(30), \
                                               Col3 varchar(30), \
                                               Col4 varchar(30)\
                                               )"

    try:
        createStmt = ibm_db.exec_immediate(conn, createQuery)
        print ("Table created successfully")
    except:
        print ("Table creation failed")

except:
    print ("Unable to connect: ", ibm_db.conn_errormsg() )

ibm_db.close(conn)
print ("Connection closed")
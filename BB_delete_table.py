﻿"""
Just a .py file for manipulating the table remotely: deleting data from table
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


    #Deleting only the rows which meet some criteria
##    DeleteQuery = "delete from "+TABLENAME+" WHERE id="+'EXAMPLE'
##    DeleteStmt = ibm_db.exec_immediate(conn, DeleteQuery)

    # Or you may just want to delete everything:
    DeleteQuery = "delete from "+TABLENAME
    DeleteStmt = ibm_db.exec_immediate(conn, DeleteQuery)

    
    #Checking the result
    selectQuery = "select * from "+TABLENAME
    selectStmt = ibm_db.exec_immediate(conn, selectQuery)

    #Fetch the Dictionary, if the only row is enough for you
    #ibm_db.fetch_both(selectStmt)

    #Fetch all the rows and print the first([0]) and the second ("USERNAME") columns for those rows
    while ibm_db.fetch_row(selectStmt) != False:
        print (" ID:",  ibm_db.result(selectStmt, 0), " @username:",  ibm_db.result(selectStmt, "USERNAME"))

except:
    print ("something went wrong, but I don't know what exactly ", ibm_db.conn_errormsg() )

ibm_db.close(conn)
print ("Connection closed")
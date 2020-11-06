"""
BolnichkaBot settings,
    База: Star_Data_test,
    расположение: rainydawn
    Имя таблицы: BB_table
"""

'''BolnichkaBot token'''
TOKEN='1479116142:AAHn7PYK_PPzxmdF-W5I1L48M1_meH1qc9Q'

'''Database connection credentials'''
#Connecting to dashDB or DB2 database requires the following information:
#Driver Name
#Database name
#Host DNS name or IP address
#Host port
#Connection protocol
#User ID (or username)
#User Password

#DSN — имя источника данных, структуры данных, используемые для описания соединения с источником данных.

'''База: Star_Data_test,
   расположение: rainydawn
'''
#{
#  "db": "BLUDB",
#  "dsn": "DATABASE=BLUDB;HOSTNAME=dashdb-txn-sbox-yp-lon02-15.services.eu-gb.bluemix.net;PORT=50000;PROTOCOL=TCPIP;UID=xxr30091;PWD=t6ngb3lrd+s6f22q;",
#  "host": "dashdb-txn-sbox-yp-lon02-15.services.eu-gb.bluemix.net",
#  "hostname": "dashdb-txn-sbox-yp-lon02-15.services.eu-gb.bluemix.net",
#  "https_url": "https://dashdb-txn-sbox-yp-lon02-15.services.eu-gb.bluemix.net:8443",
#  "jdbcurl": "jdbc:db2://dashdb-txn-sbox-yp-lon02-15.services.eu-gb.bluemix.net:50000/BLUDB",
#  "parameters": {},
#  "password": "t6ngb3lrd+s6f22q",
#  "port": 50000,
#  "ssldsn": "DATABASE=BLUDB;HOSTNAME=dashdb-txn-sbox-yp-lon02-15.services.eu-gb.bluemix.net;PORT=50001;PROTOCOL=TCPIP;UID=xxr30091;PWD=t6ngb3lrd+s6f22q;Security=SSL;",
#  "ssljdbcurl": "jdbc:db2://dashdb-txn-sbox-yp-lon02-15.services.eu-gb.bluemix.net:50001/BLUDB:sslConnection=true;",
#  "uri": "db2://xxr30091:t6ngb3lrd%2Bs6f22q@dashdb-txn-sbox-yp-lon02-15.services.eu-gb.bluemix.net:50000/BLUDB",
#  "username": "xxr30091"
#}

'''Define the credentials'''
dsn_hostname = "dashdb-txn-sbox-yp-lon02-15.services.eu-gb.bluemix.net"
dsn_uid = "xxr30091"
dsn_pwd = "t6ngb3lrd+s6f22q"

dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "BLUDB"
dsn_port = "50000"
dsn_protocol = "TCPIP"


'''Create the dsn connection string
   DSN — имя источника данных, структуры данных, используемые для описания соединения с источником данных.
'''
dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd)

#print the connection string to check correct values are specified
print(dsn)
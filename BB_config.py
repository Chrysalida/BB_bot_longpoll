"""BolnichkaBot settings,
    База: Star_Data_test,
    расположение: rainydawn
    Имя таблицы: BB_table
"""

Logpath='C:\\Users\EKAU.STARSPB\Desktop\BolnichkaBot\BB_log.log'

'''BolnichkaBot token'''
TOKEN='1479116142:AAHn7PYK_PPzxmdF-W5I1L48M1_meH1qc9Q'

'''BolnichkaBot tablename'''
TABLENAME="BB_table" #"XXR30091.BB_TABLE"


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

#user's message update json sample:
#{'content_type': 'text', 'message_id': 108, 'from_user': {'id': 591342003, 'is_bot': False, 'first_name': 'Kathy', 'username': 'NoWord', 'last_name': None, 'language_code': 'ru', 'can_join_groups': None, 'can_read_all_group_messages': None, 'supports_inline_queries': None}, 'date': 1599125237, 'chat': {'id': 591342003, 'type': 'private', 'title': None, 'username': 'NoWord', 'first_name': 'Kathy', 'last_name': None, 'all_members_are_administrators': None, 'photo': None, 'description': None, 'invite_link': None, 'pinned_message': None, 'permissions': None, 'slow_mode_delay': None, 'sticker_set_name': None, 'can_set_sticker_set': None}, 'forward_from': None, 'forward_from_chat': None, 'forward_from_message_id': None, 'forward_signature': None, 'forward_date': None, 'reply_to_message': None, 'edit_date': None, 'media_group_id': None, 'author_signature': None, 'text': 'Hi', 'entities': None, 'caption_entities': None, 'audio': None, 'document': None, 'photo': None, 'sticker': None, 'video': None, 'video_note': None, 'voice': None, 'caption': None, 'contact': None, 'location': None, 'venue': None, 'animation': None, 'dice': None, 'new_chat_member': None, 'new_chat_members': None, 'left_chat_member': None, 'new_chat_title': None, 'new_chat_photo': None, 'delete_chat_photo': None, 'group_chat_created': None, 'supergroup_chat_created': None, 'channel_chat_created': None, 'migrate_to_chat_id': None, 'migrate_from_chat_id': None, 'pinned_message': None, 'invoice': None, 'successful_payment': None, 'connected_website': None, 'json': {'message_id': 108, 'from': {'id': 591342003, 'is_bot': False, 'first_name': 'Kathy', 'username': 'NoWord', 'language_code': 'ru'}, 'chat': {'id': 591342003, 'first_name': 'Kathy', 'username': 'NoWord', 'type': 'private'}, 'date': 1599125237, 'text': 'Hi'}}
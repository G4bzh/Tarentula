	
# -*- coding: utf-8 -*- 
import jinja2
from mail.mail import sendpost
import ConfigParser
import sqlite3
import sys

reload(sys)  
sys.setdefaultencoding('utf8')

tplLoader = jinja2.FileSystemLoader(searchpath='./templates')
tplEnv = jinja2.Environment(loader=tplLoader)

tplVars = {
    'parts': range(1,11),
    'lines' : range(5,8),
   	'keywords' : ('cats', 'kitten', 'cat', 'pussy', 'kitty', 'puss'),
}

template = tplEnv.get_template( "body.jinja" )
body = template.render(tplVars)


config = ConfigParser.ConfigParser()
config.read('./mysettings.ini')
server = config.get('MAIL','server')
user   = config.get('MAIL','username')
password = config.get('MAIL','password')
recipient = config.get('MAIL','recipient')
debug = config.get('MAIL','debug')
dbpath = config.get('DB','path')


conn = sqlite3.connect(dbpath)
cursor = conn.cursor()
cursor.execute("""
	SELECT * FROM content WHERE posted=0 LIMIT 1
	""")
metadata = cursor.fetchone()


subject = metadata[3] + '¤' + metadata[1]
sendpost(recipient, user, subject, body, metadata[4], server, password, debug)

cursor.execute("""
	UPDATE content SET posted = 1 WHERE id = ?
	""",(metadata[0],))

 
conn.commit()
cursor.close()
conn.close()
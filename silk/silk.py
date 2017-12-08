	
# -*- coding: utf-8 -*- 
import jinja2
import smtplib
import email.utils
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
import getpass
import ConfigParser
import sqlite3
import sys
import urllib

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
dbpath = config.get('DB','path')

conn = sqlite3.connect(dbpath)
cursor = conn.cursor()
cursor.execute("""
	SELECT * FROM content WHERE posted=0 LIMIT 1
	""")
metadata = cursor.fetchone()



# Create the message
msg = MIMEMultipart()
msg.set_unixfrom(user)
msg['To'] = email.utils.formataddr(('Recipient', recipient))
msg['From'] = email.utils.formataddr(('Post', user))
msg['Subject'] = metadata[3] + '¤' + metadata[1]

msg.attach(MIMEText(body))

f = 'test.jpg'
urllib.urlretrieve( metadata[4], f)

part = MIMEBase('application', "octet-stream")
part.set_payload( open(f,"rb").read() )
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="test.jpg"')
msg.attach(part)

server = smtplib.SMTP(server)
try:
    server.set_debuglevel(True)

    # identify ourselves, prompting server for supported features
    server.ehlo()

    # If we can encrypt this session, do it
    if server.has_extn('STARTTLS'):
        server.starttls()
        server.ehlo() # re-identify ourselves over TLS connection

    server.login(user, password)
    server.sendmail(user, recipient, msg.as_string())
finally:
    server.quit()
    cursor.execute("""
		UPDATE content SET posted = 1 WHERE id = ?
		""",(metadata[0],))

 
conn.commit()
cursor.close()
conn.close()
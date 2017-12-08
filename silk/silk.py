import jinja2
import smtplib
import email.utils
from email.mime.text import MIMEText
import getpass
import ConfigParser


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

# Create the message
msg = MIMEText(body)
msg.set_unixfrom(user)
msg['To'] = email.utils.formataddr(('Recipient', recipient))
msg['From'] = email.utils.formataddr(('Post', user))
msg['Subject'] = 'Hello Cat'

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
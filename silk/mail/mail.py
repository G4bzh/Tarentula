import smtplib
import email.utils
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
import urllib


def sendpost(to, user, subject, body, url, server, password, debug):
	
	msg = MIMEMultipart()
	msg.set_unixfrom(user)
	msg['To'] = email.utils.formataddr(('Recipient', to))
	msg['From'] = email.utils.formataddr(('Post', user))
	msg['Subject'] = subject

	msg.attach(MIMEText(body))

	f = 'post.jpg'
	urllib.urlretrieve( url, f)

	part = MIMEBase('application', "octet-stream")
	part.set_payload( open(f,"rb").read() )
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', 'attachment; filename="' + f + '"')
	msg.attach(part)


	server = smtplib.SMTP(server)
	try:
	    server.set_debuglevel(debug)

	    # identify ourselves, prompting server for supported features
	    server.ehlo()

	    # If we can encrypt this session, do it
	    if server.has_extn('STARTTLS'):
	        server.starttls()
	        server.ehlo() # re-identify ourselves over TLS connection

	    server.login(user, password)
	    server.sendmail(user, to, msg.as_string())
	finally:
	    server.quit()
import smtplib
import email.utils
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
import urllib
import base64


def sendpost(to, user, subject, body, url, server, password, debug):
	
	msg = MIMEMultipart()
	msg.set_unixfrom(user)
	msg['To'] = email.utils.formataddr(('Recipient', to))
	msg['From'] = email.utils.formataddr(('Post', user))
	msg['Subject'] = subject

	msg.attach(MIMEText(body))

	part = MIMEBase('application', "octet-stream")
	# Cannot set the base64 png directly because \r\n are needed in the payload
	part.set_payload( url.decode('base64') )
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', 'attachment; filename="post.png"')
	msg.attach(part)

	srv = smtplib.SMTP(server)

	try:
		srv.set_debuglevel(debug)

		# identify ourselves, prompting server for supported features
		srv.ehlo()

		# If we can encrypt this session, do it
		if srv.has_extn('STARTTLS'):
		    srv.starttls()
		    srv.ehlo() # re-identify ourselves over TLS connection

		srv.login(user, password)
		srv.sendmail(user, to, msg.as_string())	

	except smtplib.SMTPException:
		raise ValueError

	finally:
		srv.quit()
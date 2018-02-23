	
# -*- coding: utf-8 -*- 
import jinja2
from mail.mail import sendpost
from contextlib import closing
import ConfigParser
import sqlite3
import sys, getopt




def main(argv):

    reload(sys)  
    sys.setdefaultencoding('utf8')
    section = 'CATS'

    opts, args = getopt.getopt(argv,"s:")
    for opt,arg in opts:
        section = arg.upper()


    tplLoader = jinja2.FileSystemLoader(searchpath='./templates')
    tplEnv = jinja2.Environment(loader=tplLoader)


    config = ConfigParser.ConfigParser()
    config.read('./mysettings.ini')
    server = config.get(section,'server')
    user   = config.get(section,'username')
    password = config.get(section,'password')
    recipient = config.get(section,'recipient')
    debug = config.get(section,'debug')
    dbpath = config.get(section,'dbpath')
    kw = config.get(section,'keywords').split(",")


    try:
        with closing(sqlite3.connect(dbpath, timeout=1)) as conn:

            cursor = conn.cursor()
            cursor.execute("""
            	SELECT * FROM content WHERE posted=0 LIMIT 1
            	""")
            metadata = cursor.fetchone()

            tplVars = {
                'parts': range(1,11),
                'lines' : range(5,8),
                'title' : metadata[2],
                'keywords' : kw
            }

            template = tplEnv.get_template( "meta.jinja" )
            meta = template.render(tplVars)

            subject = metadata[2] + '¤' + metadata[1] + '¤' + kw[0] + '¤' + meta 

            template = tplEnv.get_template( "body.jinja" )
            body = template.render(tplVars)

            sendpost(recipient, user, subject, body, metadata[3], server, password, debug)

            cursor.execute("""
            	UPDATE content SET posted = 1 WHERE id = ?
            	""",(metadata[0],))

         
            conn.commit()
            cursor.close()


    except ValueError:
        raise Exception( "Failed to send post")

    except sqlite3.Error,e:
        raise Exception( "Error in silk: %s" % e)

if __name__ == "__main__":
   main(sys.argv[1:])
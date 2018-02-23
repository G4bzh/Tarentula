# FLASK_APP=server.py flask run --host 0.0.0.0

from flask import Flask
from flask import request
import base64
import sqlite3
from contextlib import closing
import hashlib
import ConfigParser


app = Flask(__name__)

config = ConfigParser.ConfigParser()
config.read('./mysettings.ini')
# Get sections in lower case
sections = [i.lower() for i in config.sections()]

@app.before_first_request
def db_create():
    try:

        conn = sqlite3.connect("output.db")
        cursor = conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS content(
        id TEXT PRIMARY KEY UNIQUE,
        url TEXT,
        title TEXT,
        thumb BLOB,
        posted INTEGER
        )
        """)
        conn.commit()

        cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_posted
        ON content(posted)
        """)
        conn.commit()

    except sqlite3.Error,e:
        raise Exception( "Error creating DB: %s" % e)

    finally:
        cursor.close()
        conn.close()       


@app.route('/title/<section>', methods=['POST'])
def get_title(section):
    if section in sections:
        # Get JSON data
        data = request.get_json()
        title = data['title'].encode('utf8') 

        txtfile = config.get(section.upper(),'titlepath')

        with open(txtfile, "a") as f:
            f.write(title)
            f.write('\n')

        return 'OK Title'
    else:
        return 'Error Title'


@app.route('/post/<section>', methods=['POST'])
def get_post(section):
    if section in sections:    
        # Get JSON data
        data = request.get_json()

        # remove "data:image/png;base64,"
        img_data = data['img'][22:] 

        #with open("imageToSave.png", "wb") as f:
        #    f.write(img_data.decode('base64'))

        title = data['title'].encode('utf8') 

        txtfile = config.get(section.upper(),'titlepath')
        dbpath = config.get(section.upper(),'dbpath')

        with open(txtfile, "a") as f:
            f.write(title)
            f.write('\n')    

        conn = sqlite3.connect(dbpath)
        cursor = conn.cursor()

        try:
            
            cursor.execute("""
            INSERT INTO content(id, url, title, thumb, posted) VALUES(?, ?, ?, ?, ?)
            """, (hashlib.sha1(data['url']).hexdigest(), data['url'], data['title'], img_data, 0))
            
        except sqlite3.IntegrityError:
            # Key already exists (id est URL already scrapped), do nothing
            pass
            
        finally:
            conn.commit()
            cursor.close()
            conn.close() 


        return 'OK DB'
    else:
        return 'Error DB'


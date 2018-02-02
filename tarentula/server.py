# FLASK_APP=server.py flask run --host 0.0.0.0

from flask import Flask
from flask import request
import base64

app = Flask(__name__)

@app.route('/post', methods=['POST'])
def show_post():
    # show the post with the given id, the id is an integer
    data = request.get_json()

    # remove "data:image/png;base64,"
    img_data = data['img'][22:] 

    with open("imageToSave.png", "wb") as f:
    	f.write(img_data.decode('base64'))
    return 'OK'

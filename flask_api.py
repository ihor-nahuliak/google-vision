from flask import Flask, request, send_file
from google_api import Vision
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
import os

def publish_callback(result, status):
    print(result, status)
    # Handle PNPublishResult and PNStatus

app = Flask(__name__)

@app.route('/', methods=['POST'])
def process_image():
    file = request.files['pic']
    filename = file.filename

    path = os.getcwd() + '/temp/{0}'.format(filename)

    file.save(path)
    value = Vision(path).run_process()
    mood = value[0]
    score = value[1]

    pnconfig = PNConfiguration()
    pnconfig.subscribe_key = "sub-c-9cbba3d6-a053-11e7-96f6-d664df0bd9f6"
    pnconfig.publish_key = "pub-c-b8445efe-d010-4c8a-85d7-59dd061bea13"
    pnconfig.ssl = False
    pubnub = PubNub(pnconfig)

    data = {}
    data["result-url"] = "http://{0}:5000/image/{1}".format(request.remote_addr, filename)

    if mood == 'joyful':
        data["box-id"] = 1
        data["mood"] = mood
    elif mood == 'angry':
        data["box-id"] = 2
        data["mood"] = mood
    elif mood == 'blurred':
        data["box-id"] = 3
        data["mood"] = mood
    elif mood == 'sorrow':
        data["box-id"] = 4
        data["mood"] = mood
    elif mood == 'outstanding in a hat':
        data["box-id"] = 5
        data["mood"] = mood


    pubnub.publish().channel("parcelbox").message(data).sync()

@app.route('/image/<filename>')
def get_image(filename):
    path = os.getcwd() + '/temp/{0}'.format(filename)
    return send_file(path, mimetype='image/jpg')


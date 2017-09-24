from flask import Flask, request
from google_api import Vision
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

def publish_callback(result, status):
    print(result, status)
    # Handle PNPublishResult and PNStatus

app = Flask(__name__)

@app.route('/', methods=['POST'])
def process_image():
    if request.method == 'POST':
        file = request.files['pic']
        filename = file.filename
        file.save('/home/slippy/Dokumenty/{0}'.format(filename))
        r = '/home/slippy/Dokumenty/{0}'.format(filename)
        value = Vision(r).run_process()
        mood = value[0]
        score = value[1]
        print('mood: {0}, score: {1}'.format(mood, score))

        pnconfig = PNConfiguration()
        pnconfig.subscribe_key = "sub-c-9cbba3d6-a053-11e7-96f6-d664df0bd9f6"
        pnconfig.publish_key = "pub-c-b8445efe-d010-4c8a-85d7-59dd061bea13"
        pnconfig.ssl = False
        pubnub = PubNub(pnconfig)
        data = {}
        if mood == 'joyful':
            data["box-id"] = 1
            data["mood"] = mood
            data["result-url"] = "satrst"
        elif mood == 'angry':
            data["box-id"] = 2
            data["mood"] = mood
            data["result-url"] = "satrst"
        elif mood == 'blurred':
            data["box-id"] = 3
            data["mood"] = mood
            data["result-url"] = "satrst"
        elif mood == 'sorrow':
            data["box-id"] = 4
            data["mood"] = mood
            data["result-url"] = "satrst"
        elif mood == 'outstanding in a hat':
            data["box-id"] = 5
            data["mood"] = mood
            data["result-url"] = "satrst"


        pubnub.publish().channel("parcelbox").message(data).sync()


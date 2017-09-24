from flask import Flask, request, send_file
from google_api import Vision
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
import os
from PIL import Image, ImageDraw
def publish_callback(result, status):
    print(result, status)
    # Handle PNPublishResult and PNStatus

app = Flask(__name__)

def clearLine(line, title):
    line = line.replace(title, "")
    line = line.replace(" ", "")
    line = line.replace(":", "")
    line = line.replace("\n", "")
    line = line.replace("{", "")
    line = line.replace("}", "")
    return line

def parseLandmarks(path):
    f = open(path, 'r+')

    nextLandmark = ""
    foundLandmark = 0
    foundLandmarkX = ""
    foundLandmarkY = ""

    landmarks = {}

    for line in f:

        if "landmarks" in line:
            foundLandmark = 1

        elif foundLandmark == 1:
            nextLandmark = clearLine(line, "type")
            foundLandmark = 2

        elif foundLandmark == 2:
            foundLandmark = 3

        elif foundLandmark == 3:
            foundLandmarkX = clearLine(line, "x")
            foundLandmark = 4

        elif foundLandmark == 4:
            foundLandmarkY = clearLine(line, "y")
            landmarks[nextLandmark] = (foundLandmarkX, foundLandmarkY)
            foundLandmark = 0

    return landmarks

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
    data["filename"] = filename
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
    elif mood == "under_exposed":
        data["box-id"] = 6
        data["mood"] = mood



    pubnub.publish().channel("parcelbox").message(data).sync()

@app.route('/image/<filename>')
def get_image(filename):
    path = os.getcwd() + '/temp/{0}'.format(filename)

    googleResultPath = os.getcwd() + '/test.txt'
    landmarks = parseLandmarks(googleResultPath)

    print(landmarks)

    image = Image.open(path)
    draw = ImageDraw.Draw(image)

    (x, y, r) = (landmarks["LEFT_EYE"][0], landmarks["LEFT_EYE"][1], 30)
    draw.ellipse((x - r, y - r, x + r, y + r), fill=(255, 0, 0, 255))

    (x, y, r) = (landmarks["RIGHT_EYE"][0], landmarks["RIGHT_EYE"][1], 30)
    draw.ellipse((x - r, y - r, x + r, y + r), fill=(255, 0, 0, 255))

    (x1, x2, y1, y2, w) = (landmarks["LEFT_OF_LEFT_EYEBROW"][0], landmarks["LEFT_OF_LEFT_EYEBROW"][1], landmarks["RIGHT_OF_LEFT_EYEBROW"][0], landmarks["RIGHT_OF_LEFT_EYEBROW"][1], 20)
    draw.line((100,200, 150, 300), fill=128, width=w)

    (x1, x2, y1, y2, w) = (landmarks["LEFT_OF_RIGHT_EYEBROW"][0], landmarks["LEFT_OF_RIGHT_EYEBROW"][1], landmarks["RIGHT_OF_RIGHT_EYEBROW"][0], landmarks["RIGHT_OF_RIGHT_EYEBROW"][1], 20)
    draw.line((100,200, 150, 300), fill=128, width=w)

    newFile = '%s-out.jpg' % filename
    image.save(newFile)

    return send_file(newFile, mimetype='image/jpg')


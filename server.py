from flask import Flask, request
import os
app = Flask(__name__)

from Vision import detect_face

@app.route('/', methods=['POST'])
def main():
    if request.method == 'POST':
        file = request.files['pic']
        filename = file.filename
        file.save(os.path.join(os.environ['IMAGE_LOCATION'], filename))

        detect_face()

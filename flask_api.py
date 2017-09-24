from flask import Flask, request
import os
from google_api import Vision


app = Flask(__name__)

@app.route('/', methods=['POST'])
def process_image():
    if request.method == 'POST':
        file = request.files['pic']
        filename = file.filename
        file.save('/home/slippy/Dokumenty/{0}'.format(filename))
        r = '/home/slippy/Dokumenty/{0}'.format(filename)
        Vision(r).run_process()
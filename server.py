from flask import Flask, request
import os
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def GetNoteText():
    print(request)
    if request.method == 'POST':
        file = request.files['pic']
        filename = file.filename
        file.save(os.path.join(os.environ['UPLOAD_FOLDER'], filename))
        # processImage(filename)            
    else:
        return "Y U NO USE POST?"
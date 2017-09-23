from PIL import Image, ImageDraw
from google.cloud import vision
from google.cloud.vision import types, client
from oauth2client.client import GoogleCredentials
import json

input_filename = '/home/slippy/Dokumenty/sw.jpg'
max_results=1

def detect_face(url, max_results=4):
    """Uses the Vision API to detect faces in the given file.
    Args:
        face_file: A file-like object containing an image with faces.
    Returns:
        An array of Face objects with information about the picture.
    """
    # [START get_vision_service]
    client = vision.ImageAnnotatorClient()
    # [END get_vision_service]

    #content = face_file.read()
    #image = types.Image(content=content)
    request = {'image': {'source': {'image_uri': '{}'.format(url)},},}

    return client.annotate_image(request).face_annotations



#with open(input_filename, 'rb') as image:
url='https://farm4.staticflickr.com/3296/2760862365_45e011e538_z.jpg?zz%5Cx3d1'
face = detect_face(url, max_results)
s_face = str(face)
f = open('test.json', 'w')
f.write(s_face)
f.close()

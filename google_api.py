from PIL import Image, ImageDraw
from google.cloud import vision
from google.cloud.vision import types, client
from oauth2client.client import GoogleCredentials
import json

from processjson import Processor

class Vision:
    def detect_face(data, max_results=1):
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
        request = {'image': {'content': data}}

        face_annotations = client.annotate_image(request).face_annotations
        # process the image and return some values
        p = Processor()
        happy = p.get_joy_value()
        sad = p.get_sorrow_value()
        anger = p.get_anger_value()
        surprise = p.get_surprise_value()
        # underexp = p.get_underexposed_value()
        # blurred = p.get_blurred_value()
        # headwear = p.get_headwear_value()
        return [happy, sad, anger, surprise]
        

# face = detect_face(url, max_results)
# s_face = str(face)
# f = open('test.txt', 'w')
# f.write(s_face)
# f.close()



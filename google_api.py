from google.cloud import vision
from google.cloud.vision import types, client
from processjson import Processor
import os

class Vision:

    def __init__(self, file):
        self.input_filename = file

    def detect_face(self, face_file, max_results=4):
        """Uses the Vision API to detect faces in the given file.
        Args:
            face_file: A file-like object containing an image with faces.
        Returns:
            An array of Face objects with information about the picture.
        """
        # [START get_vision_service]
        client = vision.ImageAnnotatorClient()
        # [END get_vision_service]

        content = face_file.read()
        image = types.Image(content=content)

        #request = {'image': {'source': {'image_uri': '{}'.format(url)},},}

        return client.face_detection(image=image).face_annotations

    def run_process(self):
        max_results=1
        with open(self.input_filename, 'rb') as image:
            face = self.detect_face(image, max_results)
            s_face = str(face)
            f = open('test.txt', 'w')
            f.write(s_face)
            f.close()

            if os.path.isfile('test.txt'):
                file = open('test.txt')
                mood_set = set()
                p = Processor(file)
                joy, joy_score = p.get_joy_value()
                sorrow, sorrow_score = p.get_sorrow_value()
                anger, anger_score = p.get_anger_value()
                sur, sur_score = p.get_surprise_value()
                under_ex, under_ex_score = p.get_underexposed_value()
                blur, blur_score = p.get_blurred_value()
                hat, hat_score = p.get_headwear_value()
                mood_set.add((joy, joy_score))
                mood_set.add((sorrow, sorrow_score))
                mood_set.add((anger, anger_score))
                mood_set.add((sur, sur_score))
                mood_set.add((under_ex, under_ex_score))
                mood_set.add((blur, blur_score))
                mood_set.add((hat, hat_score))
                sorted_set = sorted(mood_set, key=lambda tup: tup[1], reverse=True)
                return sorted_set[0]
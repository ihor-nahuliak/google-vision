# Features:
#   joy_likelihood
#   sorrow_likelihood
#   anger_likelihood
#   surprise_likelihood
#   under_exposed_likelihood
#   blurred_likelihood
#   headwear_likelihood

# Score
#   UNKNOWN 	    0
#   VERY_UNLIKELY   1
#   UNLIKELY 	    2
#   POSSIBLE 	    3
#   LIKELY 	        4
#   VERY_LIKELY     5

score_dict = {'UNKNOWN':'0', 'VERY_UNLIKELY':'1', 'UNLIKELY':'2', 'POSSIBLE':'3', 'LIKELY':'4', 'VERY_LIKELY':'5'}


class Processor:

    def __init__(self, file):
        self.file = file

    def get_joy_value(self):
        for line in self.file:
            if 'joy_likelihood' in line:
                return 'joyful', score_dict[line.split(':')[1].strip()]

    def get_sorrow_value(self):
        for line in self.file:
            if 'sorrow_likelihood' in line:
                return 'sorrow', score_dict[line.split(':')[1].strip()]

    def get_anger_value(self):
        for line in self.file:
            if 'anger_likelihood' in line:
                return 'angry', score_dict[line.split(':')[1].strip()]

    def get_surprise_value(self):
        for line in self.file:
            if 'surprise_likelihood' in line:
                return 'surprised', score_dict[line.split(':')[1].strip()]

    def get_underexposed_value(self):
        for line in self.file:
            if 'under_exposed_likelihood' in line:
                return 'under_exposed', score_dict[line.split(':')[1].strip()]

    def get_blurred_value(self):
        for line in self.file:
            if 'blurred_likelihood' in line:
                return 'blurred', score_dict[line.split(':')[1].strip()]

    def get_headwear_value(self):
        for line in self.file:
            if 'headwear_likelihood' in line:
                return 'look outstanding in a hat', score_dict[line.split(':')[1].strip()]


# f = open('test.json', 'r')
# p = Processor(f)
#
# print(p.get_joy_value())
# print(p.get_sorrow_value())
# print(p.get_anger_value())
# print(p.get_surprise_value())
# print(p.get_underexposed_value())
# print(p.get_blurred_value())
# print(p.get_headwear_value())

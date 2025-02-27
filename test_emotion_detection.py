from EmotionDetection.emotion_prediction import emotion_detector

import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        joy = emotion_detector('I am glad this happened')
        self.assertEqual(joy['dominent_emotion'], 'joy')

        anger = emotion_detector('I am really mad about this')
        self.assertEqual(anger['dominent_emotion'], 'anger')

        disgust = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(disgust['dominent_emotion'], 'disgust')

        sadness = emotion_detector('I am so sad about this')
        self.assertEqual(sadness['dominent_emotion'], 'sadness')

        fear = emotion_detector('I am really afraid that this will happed')
        self.assertEqual(fear['dominent_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()

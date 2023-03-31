import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    def test_store_response(self):
        question = "what job?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response("teacher")
        self.assertIn("teacher", my_survey.responses)

    def test_store_multi_response(self):
        question = "what job?"
        my_survey = AnonymousSurvey(question)
        responses = ["teacher", "student", "writer"]
        for response in responses:
            my_survey.store_response(response)
        for response in responses: 
            self.assertIn(response, my_survey.responses)

if __name__ == "__main__":
    unittest.main()
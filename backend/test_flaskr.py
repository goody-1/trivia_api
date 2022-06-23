import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format('student', 'student', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        self.new_question = {'question': 'In which year was Africa\'s most populous country formed?',
                             'answer': '1914', 'category': 4, 'difficulty': 3}

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_categories(self):
        res = self.client().get('/categories')
        # res has properties like, data, json, status_code - use dir(res) to find out more
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_categories'])
        self.assertTrue(data['categories'])

    def test_get_category(self):
        res = self.client().get('/categories/1/questions')
        # res has properties like, data, json, status_code - use dir(res) to find out more
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['current_category'], 1)
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['categories'])

    def test_get_questions(self):
        res = self.client().get('/questions')
        # res has properties like, data, json, status_code - use dir(res) to find out more
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertFalse(data['current_category'])
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['questions'])
        self.assertTrue(data['categories'])

    def test_excess_page_number(self):
        res = self.client().get('/questions?page=20000')
        data = res.get_json()

        self.assertEqual(data['questions'], [])
        self.assertEqual(data['success'], True)

    def search_question(self):
        res = self.client().post('questions/search', json={"searchTerm": "title"})
        data = res.get_json()

        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertTrue(data['total_questions'])

    def test_404_invalid_search_input(self):
        res = self.client().post('questions/search', json={"searchTerm": "friskds"})
        data = res.get_json()

        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], "resource not found")

    def test_remove_question(self):
        res = self.client().delete('/questions/61')
        data = res.json
        # print(Question.query.all())
        question = Question.query.get(71)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['deleted'], 71)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['questions'])
        self.assertEqual(question, None)

    def test_add_question(self):
        res = self.client().post('/questions', json=self.new_question)
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['created'])
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['questions'])
        self.assertFalse(data['current_category'])
        self.assertTrue(data['categories'])

    def test_404_category_input_out_of_range(self):
        res = self.client().get('categories/100/questions')
        data = res.get_json()
        print(data, "\n\n")

        self.assertEqual(data['error'], 404)
        self.assertEqual(data['success'], False)

    def test_play_quiz(self):
        input_data = {
            'previous_questions':[2, 6],
            'quiz_category': {
                'id': 5,
                'type': 'Entertainment'
            }
        }

        res = self.client().post('/quizzes', json=input_data)
        data = res.get_json()
        # print("play_quiz", data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['question'])

        self.assertNotEqual(data['question']['id'], 2)
        self.assertNotEqual(data['question']['id'], 6)

        self.assertEqual(data['question']['category'], 5)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()

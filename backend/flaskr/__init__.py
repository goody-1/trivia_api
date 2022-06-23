import json
import os
# from unicodedata import category
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category, db

QUESTIONS_PER_PAGE = 10

def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    """
    @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    """
    CORS(app, )


    """
    @TODO: Use the after_request decorator to set Access-Control-Allow
    """
    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
        )
        return response


    """
    @TODO:
    Create an endpoint to handle GET requests
    for all available categories.
    """
    @app.route('/categories')
    def get_categories():
        categories = Category.query.order_by(Category.id).all()
        formatted_categories = [category.format() for category in categories]

        if len(categories) == 0:
            abort(404)

        return jsonify({
            'categories': {cat.id: cat.type for cat in categories},
            'success': True,
            'total_categories': len(Category.query.all())
        })


    """
    @TODO:
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.

    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions.
    """
    @app.route('/questions')
    def get_questions():
        categories = Category.query.all()
        # cat_type_list = [dictionary['type'].lower() for dictionary in categories]
        # print(cat_type_list); print(); print()

        questions = Question.query.order_by(Question.id).all()

        current_questions = paginate_questions(request, questions)
        # formatted_questions = [question.format() for question in questions]


        return jsonify({
            'questions': current_questions,
            'total_questions': len(questions),
            'current_category': [],
            'categories': {cat.id: cat.type for cat in categories},
            'success': True
        })

    """
    @TODO:
    Create an endpoint to DELETE question using a question ID.

    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page.
    """
    @app.route('/questions/<int:id>', methods=['DELETE'])
    def remove_question(id):
        try:
            question = Question.query.get(id)

            if question is None:
                abort(404)

            question.delete()
            selection = Question.query.order_by(Question.id).all()
            current_question = paginate_questions(request, selection)

            return jsonify({
                'success': True,
                'deleted': question.id,
                'questions': current_question,
                'total_questions': len(Question.query.all())
            })
        except:
          abort(422)

    """
    @TODO:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.
    """
    @app.route('/questions', methods=['POST'])
    def add_question():

        try:
            body = request.json

            question = body.get("question", None)
            answer = body.get("answer", None)
            category = body.get("category", None)
            difficulty = body.get("difficulty", None)

            question = Question(question=question, answer=answer, category=category, difficulty=difficulty)

            question.insert()

            questions = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(request, questions)
            categories = Category.query.all()

            return jsonify({
                'success': True,
                'questions': current_questions,
                'total_questions': len(questions),
                'current_category': [],
                'categories': {cat.id: cat.type for cat in categories},
                'created': question.id
            })
        except:
            abort(422)

    """
    @TODO:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    """
    @app.route('/questions/search', methods=['GET', 'POST'])
    def search_questions():
        data = request.get_json()

        try:
            if data['searchTerm']:
                search_term = data['searchTerm']

            questions = Question.query.order_by(Question.id)\
                .filter(Question.question.ilike("%{}%".format(search_term))).all()
            if questions == []:
                abort(404)

            current_questions = paginate_questions(request, questions)
            categories = Category.query.all()

            return jsonify({
                'success': True,
                'questions': current_questions,
                'total_questions': len(questions),
                'current_category': [],
                'categories': {cat.id: cat.type for cat in categories}
            })
        except:
            abort(404)

    """
    @TODO:
    Create a GET endpoint to get questions based on category.

    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    """
    @app.route('/categories/<int:id>/questions', methods=['GET'])
    # <category> is a variable, string by default or do <string:category>
    # link: https://flask.palletsprojects.com/en/2.1.x/api/#url-route-registrations
    def get_questions_by_category(id):
        category = Category.query.get(id)
        if (category is None):
            abort(404)

        categories = [category.format() for category in Category.query.all()]
        # cat_type_list = [dictionary['type'].lower() for dictionary in categories]
        # print(cat_type_list); print(); print()

        # if category.lower() not in cat_type_list:
        #     return abort(404)
        # category_id = db.session.query(Category)\
        #     .filter(Category.type == category.title()).first().id
        # questions = Question.query.order_by(Question.id).filter(Question.category == category_id).all()
        questions = Question.query.order_by(Question.id).filter(Question.category == id).all()
        current_questions = paginate_questions(request, questions)
        # formatted_questions = [question.format() for question in questions]

        return jsonify({
            'questions': current_questions,
            'total_questions': len(questions),
            'current_category': id,
            'categories': categories,
            'success': True
        })

    """
    @TODO:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    """
    @app.route('/quizzes', methods=['POST'])
    def get_quizzes():
        # This endpoint should take category and previous question parameters
        try:
            body = request.get_json()
            print(body, "\n\n")

            previous_questions = body.get('previous_questions', None)
            print(previous_questions)
            quiz_category = body.get('quiz_category', None)
            print("quiz category", quiz_category)
            category_id = quiz_category['id']
            print("category id", category_id)

            if category_id != 0:
                questions = Question.query.filter_by(category=category_id).all()
            else:
                questions = Question.query.all()


            def get_random_question():
                question = random.choice(questions).format()
                return question

            next_question = get_random_question()

            used = False
            if next_question['id'] in previous_questions:
                used = True

            while used:
                next_question = random.choice(questions).format()

                if (len(previous_questions) == len(questions)):
                    return jsonify({
                        'success': True,
                        'message': "Game Over"
                    }), 200

            return jsonify({
                'success': True,
                'question': next_question
            })

        except Exception as e:
            print(e)
            abort(422)

    """
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"success": False, "error": 404, "message": "resource not found"}), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({"success": False, "error": 422, "message": "unprocessable"}), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"success": False, "error": 400, "message": "bad request"}), 400

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({"success": False, "error": 405, "message": "method not allowed"}), 405

    @app.errorhandler(500)
    def internal_server(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': 'Sorry, the fault is from us not you. Please check after some time'
        }), 500

    return app


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
    @DONE: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    """
    CORS(app, )


    """
    @DONE: Use the after_request decorator to set Access-Control-Allow
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
    @Done:
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
    @DONE:
    Get paginated questions
    """
    @app.route('/questions')
    def get_questions():
        categories = Category.query.all()
        # cat_type_list = [dictionary['type'].lower() for dictionary in categories]
        # print(cat_type_list); print(); print()

        questions = (Question.query.order_by(Question.id).all())
        random.shuffle(questions)

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
    @DONE
    Remove from question
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
    @DONE
    Add to questions
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
    DONE

    Search question

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
    @DONE:
    Get questions based on category.
    """
    @app.route('/categories/<int:id>/questions', methods=['GET'])
    # <category> is a variable, string by default or do <string:category>
    # Line above is no longer relevant for this code.
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
    @DONE:
    Get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.
    """
    @app.route('/quizzes', methods=['POST'])
    def get_quiz_question():
        # This endpoint should take category and previous question parameters
        try:
            body = request.get_json()
            previous_questions = body.get('previous_questions', None)
            quiz_category = body.get('quiz_category', None)
            category_id = quiz_category['id']

            # If a category is chosen get only questions in that category else, get all questions
            if category_id:
                questions = Question.query.filter_by(category=category_id).all()
            else:
                questions = Question.query.all()

            # Make the next question random
            next_question = random.choice(questions)

            # If the question is asked
            asked = False
            if next_question.id in previous_questions:
                asked = True

            # If the question has been asked before, shuffle again
            while asked:
                next_question = random.choice(questions)

                # If number of asked questions is equal to the number of total question
                #   either for a category or for all questions then the questions are exhausted
                if (len(questions) == len(previous_questions)):
                    return jsonify({
                        'success': True,
                        'previous_questions': previous_questions,
                        'final_question': True,
                    }), 200

            print(previous_questions, "\n\n")
            return jsonify({
                'success': True,
                'question': next_question.format()
            })

        except Exception as e:
            print(e)
            abort(422)

    """
    @DONE:
    Created error handlers for all expected errors
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
        return jsonify({'success': False, 'error': 500, 'message': 'server error'}), 500

    @app.errorhandler(503)
    def service_unavailable(error):
        return jsonify({'success': False, 'error': 503, 'message': 'service not available'}), 503

    return app


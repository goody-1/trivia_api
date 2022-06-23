#	Full Stack API Final Project
##	Project Description
Trivia app is an app that allows people to play trivia and see who is the most knowledgeable of the bunch. The application is able to:

1.	Display questions. All questions or questions by category. Each question is displayed along with the category, difficulty rating and can show/hide the answer.
2.	Delete questions.
3.	Add questions and require that they include question and answer text.
4.	Search for questions based on a text query string.
5.	Play the quiz game, randomizing either all questions or within a specific category.

Follow the instructions below to get started!

##	Getting Started
This project's instructions can be found in the [backend readme](backend/README.md)

###	Installing Dependencies
####	Python 3.10.4

Follow instructions to install the latest version of python for your platform in the [python docs](https://www.python.org/downloads/release/python-3104/)

####	Virtual Enviornment
It is recommended to work within a virtual environment to run this project. This keeps your dependencies for each project separate and organaized. You can check [Real Python](https://realpython.com/python-virtual-environments-a-primer/) for instructions to set up a virtual environment.

####	PIP Dependencies
Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```
pip install -r requirements.txt
```
This will install all of the required packages in the `requirements.txt` file.

#####	Key Dependencies

-	[Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

-	[SQLAlchemy](http://flask.pocoo.org/) is the Python SQL toolkit and ORM used handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

-	[Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

#####	Installing frontend dependencies
This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the frontend directory of this repository. After cloning, open your terminal and run:

```
npm install
```

##	Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:

```
psql trivia < trivia.psql
```

## Running the server
From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:
```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

#	Running Your Frontend in Dev Mode

The frontend app was built using create-react-app. In order to run the app in development mode use `npm start`. You can change the script in the `package.json` file.

Once it compiles successfully, it opens http://localhost:3000 in the browser.

#	Testing
To run the tests, run

```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```

#	API Reference
##	Getting Started
-	Backend base url: http://127.0.0.1:5000/
-	Frontend base url: http://127.0.0.1:3000/

## Endpoints
> **GET '/categories'**

-	Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
-	Example: `curl http://127.0.0.1:5000/categories`

```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "success": true,
  "total_categories": 6
}
```

> **GET '/questions'**

-	Fetches all the questions in the database. The questions are paginated with 10 questions each page.
-	Example: `curl http://127.0.0.1:5000/questions`

```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "current_category": [],
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ],
  "success": true,
  "total_questions": 22
}
```

> **DELETE '/questions/<int:id>'

-	Delete the question that was specified by its id in the url parameter.
-	Example: `curl -X DELETE http://127.0.0.1:5000/questions/59`

```
{
  "deleted": 59,
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ],
  "success": true,
  "total_questions": 21
}
```

>	**POST '/questions'**
Create a new question. The new question must have all four information.
-	Example: `curl -X POST -H "Content-Type: application/json" -d '{"question": "What is the most populous nation in Africa", "answer": "Nigeria", "difficulty": 1, "category": "5"}' http://127.0.0.1:5000/questions`

```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "created": 62,
  "current_category": [],
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ],
  "success": true,
  "total_questions": 22
}
```

>	**POST '/questions/search'**
-	User type in a string to search for a question and it will return all the questions that contain this string.
-	Example: `curl -X POST -H "Content-Type: application/json" -d '{"searchTerm": "biograph"}' http://127.0.0.1:5000/questions/search`

```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "current_category": [],
  "questions": [
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }
  ],
  "success": true,
  "total_questions": 1
}
```

> **POST '/quizzes'**
-	Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
-	Example: `curl -X POST -H "Content-Type: application/json" -d '{"previous_questions": [20], "quiz_category": {"type": "Science", "id": "1"}}' http://127.0.0.1:5000/quizzes`
```
{
  "question": {
    "answer": "Blood",
    "category": 1,
    "difficulty": 4,
    "id": 22,
    "question": "Hematology is a branch of medicine involving the study of what?"
  },
  "success": true
}
```

#	Author and Acknowledgement
Goodness Atunde contributed to the API, implementing the TODOS(__init.py__), test file(test_flaskr.py), edited some urls in the frontend and this ReadMe file.
The project and other files are credicted to [Udacity](https://www.udacity.com/)

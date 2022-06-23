#	Full Stack API Final Project
##	Project Description
Trivia app is a web application that allow people to play trivia and seeing who's the most knowledgeable of the bunch. The application is able to:

-	Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer.
-	Delete questions.
-	Add questions and require that they include question and answer text.
-	Search for questions based on a text query string.
-	Play the quiz game, randomizing either all questions or within a specific category.

Follow the instructions below to get started! Also check out my blog to see my reflection and takeaways from compeleting this project!

##	Getting Started
###	Installing Dependencies
####	Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs]

####	Virtual Enviornment
We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the python docs

####	PIP Dependencies
Once you have your virtual environment setup and running, install dependencies by naviging to the /backend directory and running:

```pip install -r requirements.txt```
This will install all of the required packages we selected within the ```requirements.txt``` file.

#####	Key Dependencies

-	Flask is a lightweight backend microservices framework. Flask is required to handle requests and responses.

-	SQLAlchemy is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

-	Flask-CORS is the extension we'll use to handle cross origin requests from our frontend server.

#####	Installing frontend dependencies
This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the frontend directory of this repository. After cloning, open your terminal and run:

```npm install```

##	Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:

```psql trivia < trivia.psql```

## Running the server
From within the backend directory first ensure you are working using your created virtual environment.


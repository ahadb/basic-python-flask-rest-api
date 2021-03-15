# Basic Python Rest API

This project features a basic minimal JSON API written in Python using the Flask package. You should use it to
learn the fundamentals of creating an API in Python, or for that matter any API as it has the usual suspects.

## What is Done

* Returns a todo-style API with all the RESTFul routes
* Data is in memory and has no DB (you can set one up, ...I will add that later)
* Has basic authentication
* Has basic logging
* Setup with a reasonable amount of unit testing, you can easily do more

This is not a full fledged production API, nor is it perfect. You can learn from it and perfect it if you'd like

##  REST Routes

All routes return `json` even your base index or `'/'` route. 

1. GET `'/'`
2. GET `'/todo/tasks'`
3. GET `/'todo/tasks/<int:task_id>'`
4. POST `'/todo/tasks'`
5. PUT `/'todo/tasks/<int:task_id>'`
6. DELETE `/'todo/tasks/<int:task_id>'`

Use cURL, Postman, or Insomnia to play around with it

##  Usage & Commands

Using Python 3.6.1, you should use `venv` and could be compatible with 2.7.1

* `git clone`
* (venv) `pip install flask flask_httpauth logging`
* `flask run`
* `python -m unittest discover`

## What You Could Do To Better It

1. Better app *patterns and *structure
2. Add a DB, Flask is agnostic so you can use any DB you like. Try SQL Lite
3. Add a login route and improve authentication
4. Improve tests for more coverage, add coverage package (via pip). 
5. Add Swagger
6. Improve the logger
7. Alter the API, do something fun and deploy it

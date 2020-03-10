# UltimateGeneratorBackend

# Project Title

## Ultimate License Key Generator

## Application description.

    Ultimate License Key Generator is a key generator program that generates unique  product licensing keys.

## Getting Started

System Requirements
Python 3 + 
Ubuntu linux

## Backend - Flask

### Application Structure

database/sqlite/app.sqlite - database file

app.py - main flask file

models.py - holds models data

schema.py - holds graphql schema structure


## Backend Database Design

Application Table

The table used is the "Key" Table with the following fields

id, name, value, created_at

Installing Flask,rsa encryption library, CORS and GraphQL dependencies

pip install flask

pip install flask-graphql flask-migrate flask-sqlalchemy graphene graphene-sqlalchemy Flask-GraphQL  flask_cors rsa

Project creation steps
export FLASK_DEBUG=True - Enable changes to reflect on reload. 
create app.py, flask by default searches for an app.py

Database setup

Am using SQlite to avoid complex database setup.

Sql Synthax

CREATE TABLE [key] (
    id         INTEGER       PRIMARY KEY
                             UNIQUE
                             NOT NULL,
    name       VARCHAR (150) UNIQUE,
    value      VARCHAR,
    created_at DATETIME      DEFAULT (CURRENT_TIMESTAMP) 
);

# Starting the application

The application can started on the terminal using the following commands
export FLASK_DEBUG=True
flask run

For Local development, the graphql endpoint can be accessed on the url " http://127.0.0.1:5000/graphql".

# Deployment with Heroku

Install heroku on your os

## Adding a Procfile

In order for us to successfully deploy any application to Heroku, we must add a Procfile to that application.


Before we can add a Procfile, we need to first install a web server called Gunicorn. Run the following command within the application folder.

> pip install gunicorn

Update the requirements file by running

pip freeze > requirements.txt

Create a new file with Procfile as the name and do not add any extension. Add this line below

web: gunicorn app:app

Continue with the rest of the process from this reference

[ href="https://devcenter.heroku.com/articles/getting-started-with-python" title="Heroku Python Setup"]

Test the application in local mode 

heroku local web

If everything goes as planned, we're done.

Go to the heroku dashboard and add a new project and deploy using the github option

# UltimateGeneratorBackend

# Project Title

## Ultimate License Key Generator

## Application description.

    Ultimate License Key Generator is a key generator program that generates unique  product licensing keys.

## Getting Started

System Requirements
Python 2.7
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

pip2 install flask

pip2 install flask-graphql flask-migrate flask-sqlalchemy graphene graphene-sqlalchemy Flask-GraphQL  flask_cors rsa

Project creation steps
EXPORT FLASK_DEBUG=True - Enable changes to reflect on reload. 
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

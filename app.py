# from flask import Flask
from flask import Flask, render_template, render_template_string,request,url_for,redirect,send_from_directory,jsonify
import json
from ast import literal_eval
from flask_graphql import GraphQLView
from models import db_session
from schema import schema
from flask_cors import CORS

app = Flask(__name__)
app.debug = True
CORS(app)

@app.route("/")
def view_keys():
    return "keys"

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)

if __name__ == '__main__':
     app.run()
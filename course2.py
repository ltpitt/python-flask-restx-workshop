#!/usr/bin/python3.6

import string
import random
import os

from flask import Flask
from flask import request
from flask_restplus import Api, Resource, fields
from werkzeug.contrib.fixers import ProxyFix

from texts import *

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

api = Api(app, version='1.0', title='flask restplus workshop', description=descriptiveTextCourse2)


@api.route('/hints') \
class hints(Resource):
    @api.doc(responses={200: 'Ok'})
    def get(self):
        return course2_hints


@api.route('/question1')
class question1(Resource):
    def get(self):
        return question2_1


@api.route('/question2')
class question2(Resource):
    def get(self):
        return question2_2


@api.route('/question3')
class Question3(Resource):
    def get(self):
        return question2_3


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='127.0.0.1', port=port)


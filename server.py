from flask import Flask
from flask import abort
from flask.ext.restful import Api
from flask.ext.restful import Resource
from flask.ext.restful import reqparse
from flask.ext.restful import fields
from flask.ext.restful import marshal
import os
from serverops import *

import hashlib
app = Flask(__name__)
api= Api(app)
userreview_fields= {
    'name': fields.String,
    'score': fields.String
}
adduser_fields = { #just need these for crafting responses
    'name': fields.String,
    'password': fields.String
}
#TODO: ADD THE URI TRIGGERS
class AddUser(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type = str, required = True, location = 'json')
        self.reqparse.add_argument('password', type = str, required = True, location = 'json')
        super(AddUser,self).__init__()
    def put(self):
        request = self.reqparse.parse_args()
        if 'name' or 'password' not in request.keys():
            abort(404)
        user = request['name']
        #insert user into database
        #make sql thing
        password = request['password']
        password = server_ops.password_gen(password)
        #insert hashed password to database

class UserReview(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type = str, required = True, location = 'json')
        self.reqparse.add_argument('score', type = str, required = False, location = 'json')
        super(UserReview, self).__init__()
        def put(self):
            request = self.reqparse.parse_args()
            user = request['name']
            score = request['score']
            #insert score under username in db
            server_ops.append_review(user,score)
        def get(self):
            #pull data from sql serv
            user = 'doot' #usfrmsql
            score= str(0)  #from sql db
            reviewclient = {
                'name': user,
                'score': score
            }
            return marshal(reviewclient,userreview_fields)






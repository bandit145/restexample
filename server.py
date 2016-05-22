from flask import Flask
from flask.ext.restful import Api
from flask.ext.restful import Resource
from flask.ext.restful import reqparse
from flask.ext.restful import fields
from flask.ext.restful import marshal

import hashlib
app = Flask(__name__)
api= Api(app)
userreview_fields= {
    'name': fields.String,
    'score': fields.int
}
adduser_fields = { #just need these for crafting responses
    'name': fields.String,
    'password': fields.String
}

class AddUser(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type = str, required = True, location = 'json')
        self.reqparse.add_argument('password', type = str, required = True, location = 'json')
        super(AddUser,self).__init__()
    def put(self):
        request = self.reqparse.parse_args()
        user = request['name']
        #insert user into database
        #make sql thing
        password = request['password']
        hashed = hashlib.pbkdf2_hmac('sha256',password,b'salt',100000)
        password = hashlib.binascii.hexlify(hashed) #TODO: test hexlify's output
        #insert hashed password to database

class UserReview(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type = str, required = True, location = 'json')
        self.reqparse.add_argument('score', type = int, required = False, location = 'json')
        super(UserReview, self).__init__()
        def put(self):
            request = self.reqparse.parse_args()
            user = request['name']
            score = request['score']
            #insert score under username
        def get(self):
            #pull data from sql serv
            user = 0 #usfrmsql
            score= 0  #from sql db
            reviewclient = {
                'name': user,
                'score': score
            }
            return {marshal(reviewclient,userreview_fields)}






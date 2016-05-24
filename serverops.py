import hashlib
import os
class server_ops:
    def append_review(self,user,score):
        #exract number of ratings from sql db
        ratingcount = 1
        if ratingcount != 0:
            #get previous score from sql server
            score += 0#score from sql server
            score= score / ratingcount
        #put score in sql server
    def password_gen(self,password):
        rand = os.urandom(24)
        hashed = hashlib.pbkdf2_hmac('sha256', password, rand, 100000)
        password = hashlib.binascii.hexlify(hashed)
        return password



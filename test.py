from flask.ext.restful import fields
from flask.ext.restful import marshal

userreview_fields= {
    'name': fields.String,
    'score': fields.int
}
user ='doot'
score =0
reviewclient = {
                'name': user,
                'score': score
            }
doot ={marshal(reviewclient,userreview_fields)}
print(doot)
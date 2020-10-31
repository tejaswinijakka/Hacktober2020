from flask import Flask,jsonify
import pymysql
from Resources.admin import AddFood,RemoveFood,AddEvents,DeleteEvents,LostFound,RLostFound
from Resources.student import Users,UserRegistration,UserLogin,SeeLost
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['PROPAGATE_EXCEPTIONS']=True
app.config['PREFERRED_URL_SCHEME']='https'
app.config['JWT_SECRET_KEY']='allrounder'
api = Api(app)
jwt = JWTManager(app)

'''@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        'error': 'authorization_required',
        "description": "Request does not contain an access token."
    }), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        'error': 'invalid_token',
        'message': 'Signature verification failed.'
    }), 401'''


api.add_resource(AddFood,'/addfood')
api.add_resource(RemoveFood,'/removefood')
api.add_resource(AddEvents,'/addevents')
api.add_resource(DeleteEvents,'/deleteevents')
api.add_resource(LostFound,'/lostfound')
api.add_resource(RLostFound,'/rlostfound')
api.add_resource(Users,'/users')
api.add_resource(UserRegistration,'/userregistration')
api.add_resource(UserLogin,'/userlogin')
api.add_resource(SeeLost,'/seelost')


if __name__=='__main__':
    app.run(debug=True)

from flask_restful import Resource,reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token,jwt_required
from flask import jsonify
from db import query

class User():
    def __init__(self,roll_no,password):
        self.roll_no=roll_no
        self.password=password


    @classmethod
    def getUserByRoll(cls,roll_no):
        result=query(f"""SELECT roll_no,password FROM hack.registration WHERE roll_no='{roll_no}'""",return_json=False)
        if len(result)>0: return User(result[0]["roll_no"],result[0]['password'])
        return None
class Users(Resource):
    @jwt_required
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('roll_no', type=str, required=True, help='roll_no Cannot be blank')
        data= parser.parse_args()

        #try:

        return query(f"""Select * from hack.registration where roll_no='{data["roll_no"]}'""")

class UserRegistration(Resource):
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('fname',type=str,required=True,help="First Name cannot be  blank!")
        parser.add_argument('lname',type=str,required=True,help="Last Name cannot be  blank!")
        parser.add_argument('roll_no',type=str,required=True,help="Roll number cannot be  blank!")
        parser.add_argument('email_id',type=str,required=True,help="Email ID cannot be  blank!")
        parser.add_argument('password',type=str,required=True,help="Password cannot be  blank!")
        data= parser.parse_args()
        try:
            x=query(f"""SELECT * FROM hack.registration WHERE roll_no='{data['roll_no']}'""",return_json=False)
            if len(x)>0: return {"message":"A registration with that Roll number already exists."}
        except:
            return {"message":"There was an error inserting into table."}
        #if(data['Previous_office']!=None and data['previous_position']!=None and data['years_of_service']!=None):
        try:
            query(f"""INSERT INTO hack.registration VALUES('{data['fname']}',
                                                                 '{data['lname']}',
                                                                 '{data['roll_no']}',
                                                                 '{data['email_id']}',
                                                                 '{data['password']}')""")
        except:
            return {"message":"There was an error inserting into table."},400
        return {"message":"Successfully Inserted."},201

class UserLogin(Resource):

    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('roll_no',type=str,required=True,help="roll cannot be blank.")
        parser.add_argument('password',type=str,required=True,help="Password cannot be blank.")
        data=parser.parse_args()
        user=User.getUserByRoll(data['roll_no'])
        if user and safe_str_cmp(user.password,data['password']):
            access_token=create_access_token(identity=user.roll_no,expires_delta=False)
            return {'access_token':access_token},200
        return {"message":"Invalid Credentials!"},400

class SeeLost(Resource):
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('item_id',type=str,required=True,help="it cannot be blank.")
        data = parser.parse_args()
        try:
            query(f"""SELECT * FROM hack.lost_obj WHERE status = str(0)""")
        except:
           return {"message":"There was an error."},500
        return {"message":"Successfully Displayed."},201

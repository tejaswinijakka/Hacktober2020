from flask_restful import Resource,reqparse
#from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token,jwt_required
from flask import jsonify
from db import query
from datetime import datetime
#x = datetime(2020-05-17 00:00:00)

class AddFood(Resource):
    def post(self):
        parser=reqparse.RequestParser()

        parser.add_argument('item',type=str,required=True,help="Food item cannot be blank.")
        parser.add_argument('price',type=int,required=True,help="Price cannot be blank.")
        parser.add_argument('Food_id',type=int,required=True,help="Food item cannot be blank.")
        data = parser.parse_args()
        try:
            query(f"""INSERT INTO hack.food VALUES('{data['item']}',
                                                            '{data['price']}',
                                                            '{data['Food_id']}')""")
        except:
            return {"message":"There was an error inserting into Food table."},500
        return {"message":"Successfully Inserted."},201

class RemoveFood(Resource):
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('Food_id',type=int,required=True,help="Food item cannot be blank.")
        data = parser.parse_args()
        try:
            query(f"""DELETE FROM hack.food WHERE Food_id = ('{data['Food_id']}')""")
        except:
            return {"message":"There was an error deleting from Food table."},500
        return {"message":"Successfully Deleted."},201

class AddEvents(Resource):
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('event_name',type=str,required=True,help="it cannot be blank.")
        parser.add_argument('event_datetime',type=str,required=True,help="it cannot be blank.")
        parser.add_argument('venue',type=str,required=True,help="it cannot be blank.")
        data = parser.parse_args()
        try:
            query(f"""INSERT INTO hack.events VALUES('{data['event_name']}',
                                                           '{data['event_datetime']}',
                                                           '{data['venue']}')""")
        except:
           return {"message":"There was an error inserting into table."},500
        return {"message":"Successfully Inserted."},201

class DeleteEvents(Resource):
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('event_name',type=str,required=True,help="it cannot be blank.")
        data = parser.parse_args()
        try:
            query(f"""DELETE FROM hack.events WHERE event_name = ('{data['event_name']}')""")
        except:
            return {"message":"There was an error deleting from table."},500
        return {"message":"Successfully Deleted."},201

class LostFound(Resource):
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('item_id',type=str,required=True,help="it cannot be blank.")
        parser.add_argument('item_name',type=str,required=True,help="it cannot be blank.")
        parser.add_argument('last_known_place',type=str,required=True,help="it cannot be blank.")
        parser.add_argument('image_link',type=str,required=True,help="it cannot be blank.")
        parser.add_argument('status',type=int,required=True,help="it cannot be blank.")
        parser.add_argument('date',type=str,required=True,help="it cannot be blank.")
        parser.add_argument('roll_no',type=str,required=True,help="it cannot be blank.")
        parser.add_argument('object_description',type=str,required=True,help="it cannot be blank.")
        data = parser.parse_args()
        try:
            query(f"""INSERT INTO hack.lost_obj VALUES('{data['item_id']}',
                                                           '{data['item_name']}',
                                                           '{data['last_known_place']}',
                                                            '{data['image_link']}',
                                                            '{data['status']}',
                                                            '{data['date']}',
                                                            '{data['roll_no']}',
                                                            '{data['object_description']}')""")
        except:
           return {"message":"There was an error inserting into table."},500
        return {"message":"Successfully Inserted."},201

class RLostFound(Resource):
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('item_id',type=str,required=True,help="it cannot be blank.")
        data = parser.parse_args()
        try:
            query(f"""DELETE FROM hack.lost_obj WHERE item_id = ('{data['item_id']}')""")
        except:
            return {"message":"There was an error deleting from table."},500
        return {"message":"Successfully Deleted."},201

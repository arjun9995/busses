from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('time',
        #type=String,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('plate',
        #type=String,
        required=True,
        help="This field cannot be left blank!"
    )

    #@jwt_required()
    def get(self, name):
        item = [x.json() for x in ItemModel.query.filter_by(name=name).all()]
        if item:
            return {'items':item}
        return {'message': 'Item not found'}, 404
# return cls.query.filter_by(name=name).first()

    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(data['plate'])

        if item is None:
            item = ItemModel(name, **data)
        else:
            item.time = data['time']
            item.plate = data['plate']

        item.save_to_db()

        return item.json()

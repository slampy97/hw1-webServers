from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

mall_put_args = reqparse.RequestParser()
mall_put_args.add_argument("id", type=int, help="id of item is required", required=True)
mall_put_args.add_argument("name", type=str, help="id of item is required", required=True)
mall_put_args.add_argument("discount", type=float, help="id of item is required", required=True)
mall = {}


def abort_item_id_not_exists(item_id):
    if item_id not in mall:
        abort(404, message="item id is not exists!")


def abort_item_exists(item_id):
    if item_id in mall:
        abort(409, message="already have item with this id")


class HelloWorld(Resource):
    def get(self, item_id):
        abort_item_id_not_exists(item_id)
        return mall[item_id]

    def put(self, item_id):
        abort_item_exists(item_id)
        args = mall_put_args.parse_args()
        mall[item_id] = args
        return mall[item_id], 201

    def delete(self, item_id):
        abort_item_id_not_exists(item_id)
        del mall[item_id]
        return '', 204


api.add_resource(HelloWorld, "/mall/<int:item_id>")

if __name__ == "__main__":
    app.run(debug=True)

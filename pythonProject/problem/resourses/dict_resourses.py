from flask_restful import reqparse, abort, Api, Resource
from flask import jsonify
from data import db_session
from data.words import Words
from resourses.parser import parserAdd


class DictResourse(Resource):
    def get(self):
        session = db_session.create_session()
        dictionary = session.query(Words).all()
        # print(dictionary[0]["author"])
        ret = {'words': [item.to_dict(
            only=("id",
                  "author",
                  "hieroglyph",
                  "translation",
                  "front_side",
                  "left_side",
                  "right_side",
                  "up_side",
                  "down_side"
                  )) for item in dictionary]}
        return jsonify(ret)

    def post(self):
        args = parserAdd.parse_args()
        session = db_session.create_session()
        word = Words(id=args["id"],
                     hieroglyph=args["hieroglyph"],
                     tranlation=args["tranlation"],
                     front_side=args["front_side"],
                     left_side=args["left_side"],
                     right_side=args["right_side"],
                     up_side=args["up_side"],
                     down_side=args["down_side"]
                     )
        session.add(word)
        session.commit()
        return jsonify({'success': 'OK'})
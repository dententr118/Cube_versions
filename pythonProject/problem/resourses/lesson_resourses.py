from flask_restful import reqparse, abort, Api, Resource
from flask import jsonify
from data import db_session
from data.lessons import Lessons, lessons_to_course
from data.users import User
from resourses.parser import parserAdd


def abort_if_news_not_found(lesson_id):
    session = db_session.create_session()
    course = session.query(Lessons).get(lesson_id)
    if not course:
        abort(404, message=f"Lesson {lesson_id} not found")


class LessonResource(Resource):
    def get(self, user_id, lesson_id):
        abort_if_news_not_found(lesson_id)
        session = db_session.create_session()
        lesson = session.query(Lessons).get(lesson_id)
        # print([item.to_dict(only=('id', 'name')) for item in list(course.lessons)])  # .to_dict(only=('id', 'name'))
        ret = {'lesson': lesson.to_dict(only=('id', 'name', 'words'))}
        ret["course"]["lessons"] = [item.to_dict(only=('id', 'name')) for item in list(lesson.words)]
        return jsonify(ret)

    def delete(self, lesson_id):
        abort_if_news_not_found(lesson_id)
        session = db_session.create_session()
        lesson = session.query(Lessons).get(lesson_id)
        session.delete(lesson)
        session.commit()
        return jsonify({'success': 'OK'})


class LessonListResource(Resource):
    def get(self, user_id):
        session = db_session.create_session()
        cur_user = session.query(User).filter(User.id == user_id).first()
        return jsonify({'lessons': [item.to_dict(
            only=('id', 'name', 'about')) for item in cur_user.lessons]})

    def post(self):
        args = parserAdd.parse_args()
        session = db_session.create_session()
        lesson = Lessons(
            id=args['id'],
            name=args['name'],
            words=args['words']
        )
        session.add(lesson)
        session.commit()
        return jsonify({'success': 'OK'})

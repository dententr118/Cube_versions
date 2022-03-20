import datetime
import sqlalchemy
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase

words_to_lesson = sqlalchemy.Table(
    'words_to_lessons',
    SqlAlchemyBase.metadata,
    sqlalchemy.Column('words', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('words.id')),
    sqlalchemy.Column('lessons', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('lessons.id'))
)


class Words(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'words'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    hieroglyph = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    tranlation = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    front_side = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    left_side = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    right_side = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    up_side = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    down_side = sqlalchemy.Column(sqlalchemy.String, nullable=True)

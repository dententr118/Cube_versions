from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField
from wtforms.fields import EmailField, PasswordField, BooleanField
from wtforms.validators import DataRequired


class CoursesForm(FlaskForm):
    name = StringField('Название курса', validators=[DataRequired()])
    about = TextAreaField("Описание")
    submit = SubmitField('Применить')


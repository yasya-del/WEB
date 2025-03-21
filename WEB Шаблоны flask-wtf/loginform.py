from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    ast_id = StringField('ID астронавта', validators=[DataRequired()])
    ast_pas = PasswordField('Пароль астронавта', validators=[DataRequired()])
    cap_id = StringField('ID капитана', validators=[DataRequired()])
    cap_pas = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')
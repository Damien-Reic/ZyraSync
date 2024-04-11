from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length

class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(),Length(
        min=4, max=20)], render_kw={"placeholder :": "Username"})

    password = PasswordField(validators=[InputRequired(),Length(
        min=4, max=80)], render_kw={"placeholder :": "Password"})

    confirm_password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=80)], render_kw={"placeholder :": "Confirm Password"})
    
    submit = SubmitField("Register")
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required

class NameForm(Form):
	name = StringField('猜猜我的名字？',validators=[Required()])
	submit = SubmitField('Submit')
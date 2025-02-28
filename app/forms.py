
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

class AddBookForm(FlaskForm):
    title=StringField('Title')
    author=StringField('Author')
    genre=StringField('Genre')
    publicationYear=StringField('PublicationYear')
    image=StringField('Image')
    isbn=StringField('ISBN')
    submit=SubmitField('AddBook')

class EditBookForm(FlaskForm):
    title=StringField('Title')
    author=StringField('Author')
    genre=StringField('Genre')
    publicationYear=StringField('PublicationYear')
    image=StringField('Image')
    isbn=StringField('ISBN')
    submit=SubmitField('AddBook')
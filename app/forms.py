from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class AddBookForm(FlaskForm):
    title=StringField('Title',validators=[DataRequired()])
    author=StringField('Author',validators=[DataRequired()])
    genre=StringField('Genre',validators=[DataRequired()])
    publicationYear=StringField('PublicationYear',validators=[DataRequired()])
    image=StringField('Image',validators=[DataRequired()])
    isbn=StringField('ISBN',validators=[DataRequired()])
    submit=SubmitField('AddBook',validators=[DataRequired()])
    

class EditBookForm(FlaskForm):
    title=StringField('Title',validators=[DataRequired()])
    author=StringField('Author',validators=[DataRequired()])
    genre=StringField('Genre',validators=[DataRequired()])
    publicationYear=StringField('PublicationYear',validators=[DataRequired()])
    image=StringField('Image',validators=[DataRequired()])
    isbn=StringField('ISBN',validators=[DataRequired()])
    submit=SubmitField('Edit Book',validators=[DataRequired()])

# class DisplayBook():

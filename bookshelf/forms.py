from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired

'''--CREATE TABLE books.kalicat(title TEXT NOT NULL, author text NOT NULL,
--isbn text NOT NULL PRIMARY KEY , owner TEXT NOT NULL,read TEXT NOT NULL,
--borrowed bool, genre TEXT NOT NULL,pages text not null);'''


class Book(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    isbn = StringField('ISBN', validators=[DataRequired()])
    owner = StringField('Owner\'s name', validators=[DataRequired()])
    read = BooleanField('Have You read the book? (tick to indicate yes)', validators=[DataRequired()])
    borrow = BooleanField('Is the book borrowed? (tick to indicate yes)', validators=[DataRequired()])
    genre = StringField('Genre', validators=[DataRequired()])
    pages = StringField('Number of pages', validators=[DataRequired()])
    submit = SubmitField('Submit Book')

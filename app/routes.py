from flask import Blueprint,render_template
from .forms import  AddBookForm
from markupsafe import Markup

main=Blueprint('main',__name__)
@main.route('/')
def home():
    return render_template('index.html',title="Home")

@main.route('/addBook')
def addBook():
    form=AddBookForm()
    return render_template('BookManagement/addBook/addBook.html',title="AddBook",form=form)

@main.route('/editBook')
def editBook():
    return render_template('BookManagement/editBook/editBook.html',title="EditBook",form=form)

@main.route('/bookHome')
def bookHome():
    return render_template("BookManagement/bookHome/bookHome.html",title="BookHome")
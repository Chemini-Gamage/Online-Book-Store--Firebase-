from flask import jsonify,Blueprint,render_template
from .forms import  AddBookForm
from markupsafe import Markup
from app.firebase import db

main=Blueprint('main',__name__)
@main.route('/')
def home():
    return render_template('index.html',title="Home")

@main.route('/addBook', methods=['GET','POST'])
def addBook():
    form=AddBookForm()
    if form.validate():
        book_data={
             "title":form.title.data,
            "author":form.author.data,
            "genre":form.genre.data,
            "publicationYear":form.publicationYear.data,
             "image":form.image.data,
            "isbn":form.isbn.data
   
        }
        #to add the book to the firestore
        db.collection("books").add(book_data)
        return jsonify({"message":"book added successfully"})
    return render_template('BookManagement/addBook/addBook.html',title="AddBook",form=form)

@main.route('/editBook')
def editBook():
    return render_template('BookManagement/editBook/editBook.html',title="EditBook",form=form)

@main.route('/bookHome')
def bookHome():
    return render_template("BookManagement/bookHome/bookHome.html",title="BookHome")
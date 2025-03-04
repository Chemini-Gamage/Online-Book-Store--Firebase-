from flask import url_for,jsonify,Blueprint,render_template,request,redirect
from .forms import  AddBookForm,EditBookForm
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


@main.route('/bookList',methods=['GET'])
def getBook():
        books_ref=db.collection("books")
        docs=books_ref.stream()
        books=[]
        for doc in docs:
            book=doc.to_dict()
            book["id"]=doc.id
            books.append(book)
        #return jsonify(books)   
        return render_template("BookManagement/bookList/getBook.html",title="BookList",books=books)


@main.route('/editBook/<book_id>', methods=['GET', 'POST'])
def editBook(book_id):
    form=EditBookForm()
    # Fetch the book from Firestore
    book_ref = db.collection("books").document(book_id)
    book = book_ref.get()
    
    if not book.exists:
        return jsonify({"error": "Book not found"}), 404

    book_data=book.to_dict()
    if request.method == 'POST':
        data=request.form
        book_ref.update({
                        'title':data['title'],
                        'author':data['author'],
                            'genre':data['genre'],
                            'publicationYear':data['publicationYear'],
                            'image':data['image'],
                            'isbn':data['isbn'],
   
        })
        return redirect(url_for('main.getBook', book_id=book_id))
        # flash("Book updated successfully!", "success")
    # return jsonify({"message": "Book updated successfully"})
    
    # If GET request, show the book details to edit
    return render_template('BookManagement/editBook/editBook.html', title="Edit Book", book=book.to_dict(), book_id=book_id,form=form)


@main.route('/deleteBook/<book_id>',methods=['POST'])
def deleteBook(book_id):
    book_ref=db.collection("books").document(book_id)
    book=book_ref.get()
    #error if no book
    if not book.exists:
     return jsonify({"error":"no book"})
    book_ref.delete()

    return redirect(url_for('main.getBook'))

@main.route('/bookHome',methods=["Get"])
def bookHome():
    def getBook():
        books_ref=db.collection("books")
        docs=books_ref.stream()
        books=[]
        for doc in docs:
            book=doc.to_dict()
            book["id"]=doc.id
            books.append(book)
        return render_template("BookManagement/bookHome/bookHome.html",title="BookHome",books=books)
    return getBook()


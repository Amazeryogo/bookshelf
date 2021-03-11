from flask import Flask,render_template,flash,redirect
from forms import  *
from config import *
from db import *

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/books')
def lmao():
    d = getbookdata()
    return render_template('all.html',data=d)



@app.route('/',methods=['GET', 'POST'])
@app.route('/index',methods=['GET', 'POST'])
def hello_world():
    form = Book()
    title = form.title.data
    author = form.author.data
    isbn = form.isbn.data
    owner = form.owner.data
    read = form.read.data
    borrow = form.borrow.data
    genre = form.genre.data
    pages = form.pages.data
    print(title,author,isbn,owner,read,borrow,genre,pages)
    print(type(owner))
    addbooks(title,author,isbn,owner,read,borrow,genre,pages)
    return render_template('book.html',title='Book',form=form)



if __name__ == '__main__':
    app.run()

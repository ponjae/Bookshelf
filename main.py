from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

all_books = []
# db = sqlite3.connect('bookshelf.db')
# cursor = db.cursor()
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(100) NOT NULL UNIQUE, author varchar(100) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute(
#     "INSERT INTO books VALUES(1, 'Harry Potter', 'J.K. Rowling', '9')")
# db.commit()


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'< Book {self.title} >'


db.create_all()

new_book = Book(id=1, title='Harry Potter', author='J.K. Rowling', rating=9.3)
db.session.add(new_book)
db.session.commit()


@app.route('/')
def home():
    return render_template('index.html', books=all_books)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_entry = {
            'title': request.form['title'],
            'author': request.form['author'],
            'rating': request.form['rating']
        }
        all_books.append(new_entry)
        return redirect(url_for('home'))

    return render_template('add.html')


if __name__ == '__main__':
    app.run(debug=True)

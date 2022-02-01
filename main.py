from crypt import methods
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = []


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

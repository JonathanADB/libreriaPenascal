from flask import Flask, render_template, request, redirect, url_for
from database import get_all_books, insert_book, delete_book

app = Flask(__name__)

@app.route('/')
def index():
    libros = get_all_books()
    return render_template('index.html', libros=libros)

@app.route('/agregar_libro', methods=['GET', 'POST'])
def agregar_libro():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        año = request.form['ano']
        insert_book(titulo, autor, año)
        return redirect(url_for('index'))
    return render_template('agregar_libro.html')

@app.route('/eliminar_libro/<int:libro_id>', methods=['POST'])
def eliminar_libro(libro_id):
    if request.method == 'POST':
        delete_book(libro_id)
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)

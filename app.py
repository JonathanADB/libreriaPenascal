from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import db, Libro

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///libros.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Crear la base de datos y las tablas si no existen
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    libros = Libro.query.all()
    return render_template('index.html', libros=libros)

@app.route('/agregar_libro', methods=['GET', 'POST'])
def agregar_libro():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        año = request.form['ano']
        libro = Libro(titulo=titulo, autor=autor, año=año)
        db.session.add(libro)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('agregar_libro.html')

if __name__ == "__main__":
    app.run(debug=True)

import sqlite3

# Función para crear la base de datos y la tabla de libros
def create_database():
    conn = sqlite3.connect('libros.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS libros (
                        id INTEGER PRIMARY KEY,
                        titulo TEXT NOT NULL,
                        autor TEXT NOT NULL,
                        año INTEGER NOT NULL
                    )''')
    conn.commit()
    conn.close()

# Función para conectar a la base de datos
def connect_db():
    return sqlite3.connect('libros.db')

# Función para ejecutar una consulta SQL y obtener todos los resultados
def execute_query(query, params=None):
    conn = connect_db()
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

# Función para ejecutar una consulta SQL que modifica la base de datos
def execute_modify_query(query, params=None):
    conn = connect_db()
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    conn.commit()
    conn.close()

# Función para obtener todos los libros
def get_all_books():
    query = "SELECT * FROM libros"
    return execute_query(query)

# Función para insertar un nuevo libro
def insert_book(titulo, autor, año):
    query = "INSERT INTO libros (titulo, autor, año) VALUES (?, ?, ?)"
    params = (titulo, autor, año)
    execute_modify_query(query, params)


# Funcion para insertar muchos libros a la vez
def insert_books(books):
    conn = connect_db()
    cursor = conn.cursor()
    query = "INSERT INTO libros (titulo, autor, año) VALUES (?, ?, ?)"
    cursor.executemany(query, books)
    conn.commit()
    conn.close()

# Función para eliminar un libro por su ID
def delete_book(libro_id):
    query = "DELETE FROM libros WHERE id = ?"
    params = (libro_id,)
    execute_modify_query(query, params)

""" # Crear la base de datos y la tabla si no existen
create_database()  """

""" initial_books = [
    ("La sombra del viento", "Carlos Ruiz Zafón", 2001),
    ("1984", "George Orwell", 1949),
    ("Cien años de soledad", "Gabriel García Márquez", 1967),
    ("El nombre del viento", "Patrick Rothfuss", 2007),
    ("Harry Potter y la piedra filosofal", "J.K. Rowling", 1997),
    ("El principito", "Antoine de Saint-Exupéry", 1943),
    ("Don Quijote de la Mancha", "Miguel de Cervantes", 1605),
    ("Orgullo y prejuicio", "Jane Austen", 1813),
    ("Crimen y castigo", "Fyodor Dostoevsky", 1866),
    ("El señor de los anillos", "J.R.R. Tolkien", 1954),
    ("El alquimista", "Paulo Coelho", 1988),
    ("Matar un ruiseñor", "Harper Lee", 1960),
    ("Las aventuras de Sherlock Holmes", "Arthur Conan Doyle", 1892),
    ("La metamorfosis", "Franz Kafka", 1915),
    ("El amor en los tiempos del cólera", "Gabriel García Márquez", 1985),
    ("Los miserables", "Victor Hugo", 1862),
    ("Crónica de una muerte anunciada", "Gabriel García Márquez", 1981),
    ("Rayuela", "Julio Cortázar", 1963),
    ("Anna Karenina", "Leo Tolstoy", 1877),
    ("Moby Dick", "Herman Melville", 1851)
]

insert_books(initial_books) """

insert_book("ELIAS", "ES un autor", 2024)
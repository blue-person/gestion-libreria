import sqlite3 as sql

db = "./libros.db"


def ejecutar_comando(comando):
    conexion = sql.connect(db)
    cursor = conexion.cursor()
    cursor.execute(comando)

    try:
        return cursor.fetchall()
    finally:
        conexion.commit()
        conexion.close()


def conectar_db():
    ejecutar_comando(
        "CREATE TABLE IF NOT EXISTS libros(id INTEGER PRIMARY KEY, titulo TEXT, autor TEXT, fecha INTEGER, codigo TEXT)"
    )


def visualizar_libros():
    librosAlmacenados = ejecutar_comando("SELECT * FROM libros")
    return librosAlmacenados


def buscar_libro(titulo, autor, fecha, codigo):
    libroRequerido = ejecutar_comando(
        f"SELECT * FROM libros WHERE titulo='{titulo}' OR autor='{autor}' OR fecha='{fecha}' OR codigo='{codigo}'"
    )
    return libroRequerido


def agregar_libro(titulo, autor, fecha, codigo):
    ejecutar_comando(
        f"INSERT INTO libros VALUES (NULL, '{titulo}', '{autor}', '{fecha}', '{codigo}')"
    )


def actualizar_datos_libro(id, titulo, autor, fecha, codigo):
    ejecutar_comando(
        f"UPDATE libros SET titulo='{titulo}', autor='{autor}', fecha='{fecha}', codigo='{codigo}' WHERE id='{id}'"
    )


def borrar_libro(id):
    ejecutar_comando(f"DELETE FROM libros WHERE id='{id}'")

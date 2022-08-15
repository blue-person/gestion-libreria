import sqlite3 as sql

db = "./libros.db"

def ejecutarComando(comando):
    conexion = sql.connect(db)
    cursor = conexion.cursor()
    cursor.execute(comando)

    try:
        resultadosBusqueda = cursor.fetchall()
        return resultadosBusqueda
    finally:
        conexion.commit()
        conexion.close()


def conectarDB():
    ejecutarComando(
        "CREATE TABLE IF NOT EXISTS libros(id INTEGER PRIMARY KEY, titulo TEXT, autor TEXT, fecha INTEGER, codigo TEXT)"
    )


def visualizarLibros():
    librosAlmacenados = ejecutarComando("SELECT * FROM libros")
    return librosAlmacenados


def buscarLibro(titulo, autor, fecha, codigo):
    libroRequerido = ejecutarComando(
        f"SELECT * FROM libros WHERE titulo='{titulo}' OR autor='{autor}' OR fecha='{fecha}' OR codigo='{codigo}'"
    )
    return libroRequerido


def agregarLibro(titulo, autor, fecha, codigo):
    ejecutarComando(
        f"INSERT INTO libros VALUES (NULL, '{titulo}', '{autor}', '{fecha}', '{codigo}')"
    )


def actualizarDatosLibro(id, titulo, autor, fecha, codigo):
    ejecutarComando(
        f"UPDATE libros SET titulo='{titulo}', autor='{autor}', fecha='{fecha}', codigo='{codigo}' WHERE id='{id}'"
    )


def borrarLibro(id):
    ejecutarComando(f"DELETE FROM libros WHERE id='{id}'")

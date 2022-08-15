from tkinter import messagebox
import tkinter as tk
import basedatos as db


# Funciones
def limpiar_ventana():
    rellenar_casillas("", "", "", "")
    visualizar_libros()


def mensaje_informacion(texto):
    tk.messagebox.showinfo("Advertencia", texto)


def mensaje_pregunta(texto):
    pregunta = tk.messagebox.askquestion("Advertencia", texto)

    if (pregunta == "yes"): return True
    else: return False


def rellenar_casillas(titulo, autor, fecha, codigo):
    entrada_titulo.delete(0, tk.END)
    entrada_titulo.insert(tk.END, titulo)

    entrada_autor.delete(0, tk.END)
    entrada_autor.insert(tk.END, autor)

    entrada_fecha.delete(0, tk.END)
    entrada_fecha.insert(tk.END, fecha)

    entrada_codigo.delete(0, tk.END)
    entrada_codigo.insert(tk.END, codigo)


def obtener_elemento_seleccionado(event):
    try:
        global id_seleccionado
        indice = lista.curselection()[0]
        libro_seleccionado = lista.get(indice)
        id_seleccionado = libro_seleccionado[0]
        rellenar_casillas(libro_seleccionado[1], libro_seleccionado[2],
                          libro_seleccionado[3], libro_seleccionado[4])

    except IndexError:
        pass


def visualizar_libros():
    lista.delete(0, tk.END)
    lista_libros = db.visualizar_libros()

    for libro in lista_libros:
        lista.insert(tk.END, libro)


def buscar_libro():
    lista.delete(0, tk.END)
    lista_libros = db.buscar_libro(titulo.get(), autor.get(), fecha.get(),
                                    codigo.get())

    for libro in lista_libros:
        lista.insert(tk.END, libro)


def agregar_libro():
    titulo_libro = titulo.get()
    try:
        db.agregar_libro(titulo_libro, autor.get(), fecha.get(), codigo.get())
        limpiar_ventana()
        mensaje_informacion(f"{titulo_libro} fue agregado satisfactoriamente")
    except:
        mensaje_informacion(
            f"Hubo un error al agregar {titulo_libro} a la base de datos")


def actualizar_datos_libro():
    titulo_libro = titulo.get()
    try:
        db.actualizar_datos_libro(id_seleccionado, titulo_libro, autor.get(),
                                   fecha.get(), codigo.get())
        limpiar_ventana()
        mensaje_informacion(
            f"{titulo_libro} fue actualizado satisfactoriamente")
    except:
        mensaje_informacion(
            f"Hubo un error al actualizar los datos de {titulo_libro} en la base de datos"
        )


def borrar_libro():
    titulo_libro = titulo.get()
    accion_confirmada = mensaje_pregunta(
        f"Se borrara {titulo_libro} de la base de datos. ¿Desea continuar?")

    if accion_confirmada:
        try:
            db.borrar_libro(id_seleccionado)
            limpiar_ventana()
            mensaje_informacion(
                f"{titulo_libro} fue eliminado satisfactoriamente")
        except:
            mensaje_informacion(
                f"Hubo un error al eliminar {titulo_libro} de la base de datos"
            )


def cerrar_programa():
    accion_confirmada = mensaje_pregunta(
        f"Cualquier dato que no se haya guardado se perdera. ¿Desea continuar?"
    )

    if accion_confirmada: principal.destroy()


# Ventana principal
principal = tk.Tk()
principal.title("Gestor de _libros")
principal.resizable(False, False)

# Etiquetas
etiqueta_titulo = tk.Label(principal, text="_titulo")
etiqueta_titulo.grid(row=0, column=0)

etiqueta_autor = tk.Label(principal, text="_autor")
etiqueta_autor.grid(row=0, column=2)

etiqueta_fecha = tk.Label(principal, text="Año")
etiqueta_fecha.grid(row=1, column=0)

etiqueta_codigo = tk.Label(principal, text="ISBN")
etiqueta_codigo.grid(row=1, column=2)

# Entradas
titulo = tk.StringVar()
entrada_titulo = tk.Entry(principal, textvariable=titulo)
entrada_titulo.grid(row=0, column=1)

autor = tk.StringVar()
entrada_autor = tk.Entry(principal, textvariable=autor)
entrada_autor.grid(row=0, column=3)

fecha = tk.StringVar()
entrada_fecha = tk.Entry(principal, textvariable=fecha)
entrada_fecha.grid(row=1, column=1)

codigo = tk.StringVar()
entrada_codigo = tk.Entry(principal, textvariable=codigo)
entrada_codigo.grid(row=1, column=3)

# Lista y Barra de desplazamiento
lista = tk.Listbox(principal, height=8, width=25)
lista.grid(
    row=2, column=0, rowspan=6, columnspan=2
)  # Empieza en X: 2, y en Y: 0, pero se expande 6 filas y 2 columnas

barra_scroll = tk.Scrollbar(principal)
barra_scroll.grid(row=2, column=2, rowspan=6)

lista.configure(yscrollcommand=barra_scroll.set)
barra_scroll.configure(command=lista.yview)

# Eventos de la lista
lista.bind("<<ListboxSelect>>", obtener_elemento_seleccionado)

# Botones
boton_visualizar = tk.Button(principal,
                             text="Visualizar",
                             width=12,
                             command=visualizar_libros)
boton_visualizar.grid(row=2, column=3)

boton_buscar = tk.Button(principal,
                         text="Buscar",
                         width=12,
                         command=buscar_libro)
boton_buscar.grid(row=3, column=3)

boton_agregar = tk.Button(principal,
                          text="Agregar",
                          width=12,
                          command=agregar_libro)
boton_agregar.grid(row=4, column=3)

boton_actualizar = tk.Button(principal,
                             text="Actualizar",
                             width=12,
                             command=actualizar_datos_libro)
boton_actualizar.grid(row=5, column=3)

boton_borrar = tk.Button(principal,
                         text="Borrar",
                         width=12,
                         command=borrar_libro)
boton_borrar.grid(row=6, column=3)

boton_cerrar = tk.Button(principal,
                         text="Cerrar",
                         width=12,
                         command=cerrar_programa)
boton_cerrar.grid(row=7, column=3)


# Bucle principal
def ejecucion_principal():
    db.conectarDB()
    principal.mainloop()
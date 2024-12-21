from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def agregar_productos(nombre, precio):
    try:
        conexion = sqlite3.connect('products.db')
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO products(name, price) VALUES (?, ?)", (nombre, precio))
        conexion.commit()
        conexion.close()
        return "El producto se agrego correctamente"
    except:
        return "Error al cargar el producto"
    
def eliminar_productos(id):
    try:
        conexion = sqlite3.connect('products.db')
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM products WHERE id = ?", (id,))
        conexion.commit()
        conexion.close()
        return 'Producto eliminado correctamente'
    except:
        return "Error al eliminar el producto"
    
def listar_productos():
    conexion = sqlite3.connect('products.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM products")
    resultados = cursor.fetchall()
    conexion.close()
    return resultados

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cargar', methods=['GET', 'POST'])
def cargar():
    mensaje = ''
    if request.method == 'POST':
        nombre = request.form['Nombre']
        precio = request.form['Precio']
        mensaje = agregar_productos(nombre, precio)
    return render_template('cargar.html', mensaje=mensaje)

@app.route('/eliminar', methods=['GET', 'POST'])
def eliminar():
    mensaje = ''
    if request.method == 'POST':
        id = request.form['ID']
        mensaje = eliminar_productos(id)
    return render_template('eliminar.html', mensaje=mensaje)

@app.route('/listar', methods=['GET'])
def listado():
    productos = listar_productos()
    return render_template('listado.html', productos=productos)
if __name__ == '__main__':
    app.run(debug=True, port=5002)
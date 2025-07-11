import sqlite3



class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_precio(self):
        return f"${self.precio:.2f}"



class Electronico(Producto):
    def mostrar_precio(self):
        return f"${self.precio:.2f} (Electrónico - incluye IVA)"

class Ropa(Producto):
    def mostrar_precio(self):
        return f"${self.precio:.2f} (Ropa - sin IVA incluido)"



conn = sqlite3.connect("productos.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT NOT NULL,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL
)
''')
conn.commit()



def guardar_producto(producto):
    cursor.execute('''
        INSERT INTO productos (tipo, nombre, precio)
        VALUES (?, ?, ?)
    ''', (producto.__class__.__name__, producto.nombre, producto.precio))
    conn.commit()

def obtener_productos():
    cursor.execute("SELECT tipo, nombre, precio FROM productos")
    filas = cursor.fetchall()

    productos = []
    for tipo, nombre, precio in filas:
        if tipo == "Electronico":
            productos.append(Electronico(nombre, precio))
        elif tipo == "Ropa":
            productos.append(Ropa(nombre, precio))
        else:
            productos.append(Producto(nombre, precio))
    return productos

p1 = Electronico("Laptop Lenovo", 1500.00)
p2 = Ropa("Camisa Polo", 35.50)

guardar_producto(p1)
guardar_producto(p2)


print("Inventario:")
for prod in obtener_productos():
    print(f"{prod.nombre} - {prod.mostrar_precio()}")

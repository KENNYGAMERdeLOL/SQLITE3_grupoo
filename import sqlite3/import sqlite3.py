#Problema 2
import sqlite3
from abc import ABC, abstractmethod

# Clase abstracta Vehiculo
class Vehiculo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @abstractmethod
    def mostrar_informacion(self):
        pass

    @abstractmethod
    def get_tipo(self):
        pass

# Clase Auto que hereda de Vehiculo
class Auto(Vehiculo):
    def mostrar_informacion(self):
        print(f"Auto - Marca: {self.marca}, Modelo: {self.modelo}")

    def get_tipo(self):
        return "Auto"

# Clase Moto que hereda de Vehiculo
class Moto(Vehiculo):
    def mostrar_informacion(self):
        print(f"Moto - Marca: {self.marca}, Modelo: {self.modelo}")

    def get_tipo(self):
        return "Moto"

# Clase para gestionar la base de datos SQLite
class DatabaseManager:
    def __init__(self, db_name='vehiculos.db'):
        self.conn = sqlite3.connect(db_name)
        self.crear_tabla()

    def crear_tabla(self):
        sql = '''
        CREATE TABLE IF NOT EXISTS vehiculos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT,
            marca TEXT,
            modelo TEXT
        )
        '''
        self.conn.execute(sql)
        self.conn.commit()

    def guardar_vehiculo(self, vehiculo):
        sql = 'INSERT INTO vehiculos (tipo, marca, modelo) VALUES (?, ?, ?)'
        self.conn.execute(sql, (vehiculo.get_tipo(), vehiculo.marca, vehiculo.modelo))
        self.conn.commit()
        print("Vehículo guardado en la base de datos.")

# Programa Principal
def main():
    db_manager = DatabaseManager()

    tipo = input("Ingrese tipo de vehículo (auto/moto): ").strip().lower()
    marca = input("Ingrese la marca: ").strip()
    modelo = input("Ingrese el modelo: ").strip()

    if tipo == 'auto':
        vehiculo = Auto(marca, modelo)
    elif tipo == 'moto':
        vehiculo = Moto(marca, modelo)
    else:
        print(" Tipo de vehículo no reconocido.")
        return

    vehiculo.mostrar_informacion()
    db_manager.guardar_vehiculo(vehiculo)

if __name__ == "__main__":
    main()
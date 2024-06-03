#Moya Albarran Laura Yuliana 010170037
#Lara Estevez Santiago 010169042
#Alberto Guzmán Barrera 010169141
#Axel Castañeda Sánchez 010145666
#Diego Sánchez Mendoza 340401995
import threading
import time

controlador_impresora = threading.Semaphore(2)

class impresora:
    def __init__(self, nombre):
        self.nombre = nombre
        self.disponible = True
        self.nodisponible = False

    def imprimir(self, tarea):
        print(f"La impresión {tarea} ha entrado a la cola de la impresora {self.nombre}")
        with controlador_impresora:
            print(f"La impresión {tarea} se está imprimiendo en {self.nombre}")
            time.sleep(20)
            print(f"La impresión {tarea} ha liberado la cola de impresión de {self.nombre}")

impresora1 = impresora("Hp")
impresora2 = impresora("Lenovo")
impresora3 = impresora("Epson")
impresora4 = impresora("Canon")

threads = []

tareas = ["Tarea 1", "Tarea 2", "Tarea 3", "Tarea 4"]

for tarea in tareas:
    thread = threading.Thread(target=impresora1.imprimir, args=(tarea,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

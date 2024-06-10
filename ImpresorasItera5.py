import threading
import time

controlador_impresora = threading.Semaphore(2)

class Impresora:
    def __init__(self, nombre):
        self.nombre = nombre
        self.disponible = True
        self.nodisponible = False

    def imprimir(self, tarea):
        print(f"La impresión {tarea} ha entrado a la cola de la impresora {self.nombre}")
        with controlador_impresora:
            print(f"La impresión {tarea} se está imprimiendo en {self.nombre}")
            time.sleep(2)  # Cambiado a 2 segundos para pruebas más rápidas
            print(f"La impresión {tarea} ha liberado la cola de impresión de {self.nombre}")

impresoras = [
    Impresora("Hp"),
    Impresora("Lenovo"),
    Impresora("Epson"),
    Impresora("Canon")
]

tareas = ["Tarea 1", "Tarea 2", "Tarea 3", "Tarea 4", "Tarea 5"]

for i in range(5):  
    threads = []
    for j, tarea in enumerate(tareas):
        impresora = impresoras[j % len(impresoras)]  
        thread = threading.Thread(target=impresora.imprimir, args=(tarea,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

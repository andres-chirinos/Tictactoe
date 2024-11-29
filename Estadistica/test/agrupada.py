import Estadistica
import random

def main():
    tabla = Estadistica.TablaNoAgrupada()
    tabla.agregar_columna("Altura", int, 0,descripcion="Altura en cm")

    for _ in range(100):
        tabla.agregar_datos([random.randint(150, 200)])
    
    print(tabla.media("Altura"))

if __name__ == "__main__":
    main()
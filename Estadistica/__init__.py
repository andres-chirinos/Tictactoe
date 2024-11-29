from tabla import Tabla
from tabla.agrupada import TablaAgrupada
from tabla.no_agrupada import TablaNoAgrupada
from tabla.correlacion import TablaCorrelacion

# from cli import CLI

import random

def main():
    tabla = TablaNoAgrupada(Tabla)
    tabla.agregar_columna("Altura", int, 0,descripcion="Altura en cm")

    # for _ in range(100):
    #     tabla.agregar_datos([random.randint(150, 200)])
    
    # tabla.exportar_datos_csv("datos.csv")
    tabla.importar_datos_csv("test/datos.csv")
    print(tabla.media("Altura"))
    print(tabla.mediana("Altura"))
    print(tabla.moda("Altura"))
    print(tabla.desviacion_media("Altura"))
    print(tabla.desviacion_mediana("Altura"))
    print(tabla.rango_cuartilico("Altura"))
    print(tabla.rango_semi_cuartilico("Altura"))

if __name__ == "__main__":
    main()
from tabulate import tabulate

class Tabla:
    def __init__(self):
        self.nombre = ""
        self.metadatos = {"columnas": [], "filas": 0, "datos": 0, "tipo": "", "descripcion": ""}
        self.datos = []

    #Importación y Exportación de Datos
    def importar_datos_csv(self, ruta)->None:
        with open(ruta, "r") as archivo:
            for linea in archivo:
                fila = linea.strip().split(",")
                fila_convertida = [self.convertir_dato(valor, self.metadatos["columnas"][i]["tipo"]) for i, valor in enumerate(fila)]
                self.datos.append(fila_convertida)
        
    def exportar_datos_csv(self, ruta)->None:
        with open(ruta, "w") as archivo:
            for fila in self.datos:
                archivo.write(",".join(map(str, fila)) + "\n")

    #Operaciones con Tablas
    def agregar_columna(self, nombre_columna, tipo=str, valor_por_defecto=None, funcion_calculo=None, descripcion:str=None)->None:
        self.metadatos["columnas"].append({"nombre": nombre_columna, "tipo": tipo, "valor_por_defecto": valor_por_defecto, "Descripcion": descripcion})
        for fila in self.datos:
            if funcion_calculo:
                valor_calculado = funcion_calculo(fila)
                fila.append(self.convertir_dato(valor_calculado, tipo))
            else:
                fila.append(self.convertir_dato(valor_por_defecto, tipo))

    def agregar_datos(self, fila)->None:
        fila_convertida = [self.convertir_dato(fila[i], self.metadatos["columnas"][i]["tipo"]) if i < len(fila) else self.metadatos["columnas"][i]["valor_por_defecto"] for i in range(len(self.metadatos["columnas"]))]
        self.datos.append(fila_convertida)

    def mostrar_datos(self)->None:
        headers = [col["nombre"] for col in self.metadatos["columnas"]]
        print(tabulate(self.datos, headers=headers, tablefmt="grid"))

    def convertir_dato(self, valor, tipo):
        try:
            return tipo(valor)
        except ValueError:
            print(f"Advertencia: No se pudo convertir el valor '{valor}' al tipo {tipo.__name__}. Usando valor por defecto.")
        return valor
    
    #Operaciones con Columnas
    def obtener_valores_columna(self, nombre_columna):
        for i, col in enumerate(self.metadatos["columnas"]):
            if col["nombre"] == nombre_columna:
                return [fila[i] for fila in self.datos]
        return None

    def obtener_valores_columna_como_subtabla(self, *nombres_columnas):
        subtabla = Tabla()  # Paso 1: Crear una nueva instancia de Tabla
        indices_columnas = []
        for nombre in nombres_columnas:
            for i, col in enumerate(self.metadatos["columnas"]):
                if col["nombre"] == nombre:
                    indices_columnas.append(i)
                    # Paso 2: Agregar la columna a la subtabla
                    subtabla.agregar_columna(nombre, col["tipo"])
                    break

        # Paso 3: Iterar sobre los datos existentes
        for fila in self.datos:
            fila_subtabla = [fila[i] for i in indices_columnas]
            subtabla.agregar_datos(fila_subtabla)  # Agregar fila a la subtabla

        # Paso 4: Retornar la nueva instancia de Tabla
        return subtabla

    #Operaciones con Filas
    def obtener_fila(self, indice):
        if indice >= 0 and indice < len(self.datos):
            return self.datos[indice]
        return None
    
    def obtener_filas(self, indices):
        filas = []
        for indice in indices:
            fila = self.obtener_fila(indice)
            if fila:
                filas.append(fila)
        return filas
    
    def eliminar_fila(self, indice):
        if indice >= 0 and indice < len(self.datos):
            del self.datos[indice]
            return True
        return False
    
    def eliminar_filas(self, indices):
        indices.sort(reverse=True)
        for indice in indices:
            self.eliminar_fila(indice)

    #Operaciones con Celdas
    def obtener_valor_celda(self, fila, columna):
        if fila >= 0 and fila < len(self.datos) and columna >= 0 and columna < len(self.metadatos["columnas"]):
            return self.datos[fila][columna]
        return None
    
    def modificar_valor_celda(self, fila, columna, valor):
        if fila >= 0 and fila < len(self.datos) and columna >= 0 and columna < len(self.metadatos["columnas"]):
            self.datos[fila][columna] = valor
            return True
        return False
    
    def eliminar_valor_celda(self, fila, columna):
        return self.modificar_valor_celda(fila, columna, self.metadatos["columnas"][columna]["valor_por_defecto"])
    
    def eliminar_valores_celda(self, celdas):
        for celda in celdas:
            self.eliminar_valor_celda(celda[0], celda[1])
    
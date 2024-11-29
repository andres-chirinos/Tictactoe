import csv
from collections import defaultdict
from collections import deque
import tabulate

class Tabla:
    def __init__(self) -> None:
        self.columnas = []
        self.registros_en_bruto = []
        self.registros_validados = []
        self.registros_evaluados = []
        pass

    def importar_csv(self, path: str, separador: str = ";", codificado: str = "utf-8"):
        with open(path, encoding=codificado) as archivo:
            lector = csv.reader(archivo, delimiter=separador)
            encabezados = next(lector)
            encabezados = [
                self.agregar_encabezado(encabezado) for encabezado in encabezados
            ]
            for fila in lector:
                self.agregar_registro(encabezados, fila)
        pass

    def agregar_encabezado(
        self,
        nombre: str,
        validado: callable = lambda x: x,
        evaluado: callable = None,
        oculto: bool = False,
        indice: int = None,
    ):
        try:
            data = {"nombre": nombre, "validado": validado, "evaluado": evaluado, "oculto": oculto}
            if indice:
                self.columnas.insert(data, indice)
                pass
            self.columnas.append(data)
            return data
        except Exception as e:
            print("WARN: ", e)
            return

    def editar_encabezado(
        self,
        nombre: str,
        validado: callable = lambda x: x,
        evaluado: callable = None,
        indice: int = None,
    ):
        try:
            for i, encabezado in enumerate(self.columnas):
                if encabezado["nombre"] == nombre:
                    encabezado["validado"] = validado
                    encabezado["evaluado"] = evaluado
                    if indice:
                        self.columnas.insert(encabezado, indice)
                        pass
                    return encabezado
            return self.agregar_encabezado(nombre, validado, evaluado, indice)
        except Exception as e:
            print("WARN: ", e)

    def agregar_registro(self, encabezados, fila):
        registro = defaultdict()
        for i, encabezado in enumerate(encabezados):
            encabezado_nombre = encabezado["nombre"]
            registro[encabezado_nombre] = fila[i]
        self.registros_en_bruto.append(registro)

    def validar(self):
        self.registros_validados = []
        for registro in self.registros_en_bruto:
            registro_validado = defaultdict()
            for encabezado in self.columnas:
                encabezado_nombre = encabezado["nombre"]
                encabezado_validado = encabezado["validado"]
                if encabezado_validado:
                    try:
                        registro_validado[encabezado_nombre] = encabezado_validado(
                            registro[encabezado_nombre]
                        )
                    except KeyError:
                        registro_validado[encabezado_nombre] = None
                else:
                    registro_validado[encabezado_nombre] = registro[encabezado_nombre]
            self.registros_validados.append(registro_validado)

    def calcular(self):
        self.registros_evaluados = self.registros_validados.copy()
        cola = deque(self.columnas)
        while cola:
            try:
                encabezado = cola.pop()
                encabezado_nombre = encabezado["nombre"]
                encabezado_evaluado = encabezado["evaluado"]
                for registro in self.registros_evaluados:
                    if encabezado_evaluado:
                        registro[encabezado_nombre] = encabezado_evaluado(**registro)
                    else:
                        registro[encabezado_nombre] = registro[encabezado_nombre]
            except KeyError as e:
                # print(e)
                if any([encabezado == columna["nombre"] for columna in self.columnas]):
                    print(f"ERROR: {encabezado} no se encuentra en los registros")
                    continue
                cola.appendleft(encabezado)

    def mostrar_tabla(self):
        headers = list(map(lambda x: x["nombre"], self.columnas))
        registros_ordenados = [
            [registro[col["nombre"]] for col in self.columnas if col["oculto"]==False]
            for registro in self.registros_evaluados
        ]
        print(tabulate.tabulate(registros_ordenados, headers=headers))

    def exportar_tabla(self, path: str):
        headers = [col["nombre"] for col in self.columnas if col["oculto"] == False]
        registros_ordenados = [
            [registro[col["nombre"]] for col in self.columnas if col["oculto"] == False]
            for registro in self.registros_evaluados
        ]
        try:
            with open(path, mode='w', newline='', encoding='utf-8') as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow(headers)
                escritor.writerows(registros_ordenados)
            print(f"Tabla exportada exitosamente a {path}")
        except Exception as e:
            self.manejar_error(e)
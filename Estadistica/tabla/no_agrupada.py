from tabla import Tabla
import math

class TablaNoAgrupada(Tabla):
    def __init__(self,datos:list = None) -> None:
        super().__init__()
        pass

    #Estadisticas
    ## Medidas de Tendencia Central
    def media(self, nombre_columna):
        valores = self.obtener_valores_columna(nombre_columna)
        return sum(valores) / len(valores)
    
    def mediana(self, nombre_columna):
        valores = self.obtener_valores_columna(nombre_columna)
        valores.sort()
        n = len(valores)
        if n % 2 == 0:
            return (valores[n // 2 - 1] + valores[n // 2]) / 2
        return valores[n // 2]
    
    def moda(self, nombre_columna):
        valores = self.obtener_valores_columna(nombre_columna)
        frecuencias = {}
        for valor in valores:
            if valor in frecuencias:
                frecuencias[valor] += 1
            else:
                frecuencias[valor] = 1
        moda = max(frecuencias, key=frecuencias.get)
        return moda, frecuencias[moda]
    
    ## Medidas de Dispersión
    def desviacion_media(self, nombre_columna):
        valores = self.obtener_valores_columna(nombre_columna)
        media = self.media(nombre_columna)
        return sum([abs(valor - media) for valor in valores]) / len(valores)
    
    def desviacion_mediana(self, nombre_columna):
        valores = self.obtener_valores_columna(nombre_columna)
        mediana = self.mediana(nombre_columna)
        return sum([abs(valor - mediana) for valor in valores]) / len(valores)
    
    def varianza_poblacional(self, nombre_columna):
        valores = self.obtener_valores_columna(nombre_columna)
        media = self.media(nombre_columna)
        return sum([(valor - media) ** 2 for valor in valores]) / len(valores)
    
    def varianza_muestral(self, nombre_columna):
        valores = self.obtener_valores_columna(nombre_columna)
        media = self.media(nombre_columna)
        return sum([(valor - media) ** 2 for valor in valores]) / (len(valores) - 1)
    
    def rango(self, nombre_columna):
        valores = self.obtener_valores_columna(nombre_columna)
        return max(valores) - min(valores)
    
    def rango_cuartilico(self, nombre_columna):
        valores = self.obtener_valores_columna(nombre_columna)
        valores.sort()
        n = len(valores)
        q1 = valores[n // 4]
        q3 = valores[3 * n // 4]
        return q3 - q1
    
    def rango_semi_cuartilico(self, nombre_columna):
        valores = self.obtener_valores_columna(nombre_columna)
        valores.sort()
        n = len(valores)
        q1 = valores[n // 4]
        q3 = valores[3 * n // 4]
        return (q3 - q1) / 2
    
    def coeficiente_varianza(self, nombre_columna):
        valores = self.obtener_valores_columna(nombre_columna)
        media = self.media(nombre_columna)
        desviacion = self.desviacion_media(nombre_columna)
        return (desviacion / media) * 100
    
    def desviacion_tipica_poblacional(self, nombre_columna):
        return math.sqrt(self.varianza_poblacional(nombre_columna))
    
    def desviacion_tipica_muestral(self, nombre_columna):
        return math.sqrt(self.varianza_muestral(nombre_columna))
    
    ## Medidas de Posición
    def cuartil(self, nombre_columna, q):
        valores = self.obtener_valores_columna(nombre_columna)
        valores.sort()
        n = len(valores)
        return valores[q * n // 4]
    
    def percentil(self, nombre_columna, p):
        valores = self.obtener_valores_columna(nombre_columna)
        valores.sort()
        n = len(valores)
        return valores[p * n // 100]
    
    def decil(self, nombre_columna, d):
        valores = self.obtener_valores_columna(nombre_columna)
        valores.sort()
        n = len(valores)
        return valores[d * n // 10]
    
    ## Medidas de Forma
    def coeficiente_apertura(self, nombre_columna):
        valores = self.obtener_valores_columna(nombre_columna)
        q1 = self.cuartil(nombre_columna, 1)
        q3 = self.cuartil(nombre_columna, 3)
        rango_cuartilico = q3 - q1
        media = self.media(nombre_columna)
        return (q3 - media) - (media - q1) / rango_cuartilico

    def recorrido_relativo(self, nombre_columna):
        valores = self.obtener_valores_columna(nombre_columna)
        return self.rango(nombre_columna) / self.media(nombre_columna)
    
    ## Medidas de Relación
    def coeficiente_correlacion(self, nombre_columna1, nombre_columna2):
        valores1 = self.obtener_valores_columna(nombre_columna1)
        valores2 = self.obtener_valores_columna(nombre_columna2)
        media1 = self.media(nombre_columna1)
        media2 = self.media(nombre_columna2)
        desviacion1 = self.desviacion_media(nombre_columna1)
        desviacion2 = self.desviacion_media(nombre_columna2)
        n = len(valores1)
        suma = sum([(valores1[i] - media1) * (valores2[i] - media2) for i in range(n)])
        return suma / (n * desviacion1 * desviacion2)
    
    def coeficiente_determinacion(self, nombre_columna1, nombre_columna2):
        return self.coeficiente_correlacion(nombre_columna1, nombre_columna2) ** 2
    
    ## Medidas Especiales
    def media_cuadratica(self, nombre_columna):
        valores = self.obtener_valores_columna(nombre_columna)
        return math.sqrt(sum([valor ** 2 for valor in valores]) / len(valores))
    
    def media_geometrica(self, nombre_columna):
        valores = self.obtener_valores_columna(nombre_columna)
        return math.pow(math.prod(valores), 1 / len(valores))
    
    def media_hiperbolica(self, nombre_columna):
        valores = self.obtener_valores_columna(nombre_columna)
        return len(valores) / sum([1 / valor for valor in valores])
    
    def recuento_estandar(self, nombre_columna):
        valores = self.obtener_valores_columna(nombre_columna)
        return len(valores)
    
    ## Análisis de Regresión
    def regresion_lineal(self, nombre_columna1, nombre_columna2):
        valores1 = self.obtener_valores_columna(nombre_columna1)
        valores2 = self.obtener_valores_columna(nombre_columna2)
        n = len(valores1)
        sum_x = sum(valores1)
        sum_y = sum(valores2)
        sum_xy = sum([valores1[i] * valores2[i] for i in range(n)])
        sum_x2 = sum([valor ** 2 for valor in valores1])
        sum_y2 = sum([valor ** 2 for valor in valores2])
        m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
        b = (sum_y - m * sum_x) / n
        return m, b
    
    def regresion_inversa(self, nombre_columna1, nombre_columna2):
        valores1 = self.obtener_valores_columna(nombre_columna1)
        valores2 = self.obtener_valores_columna(nombre_columna2)
        n = len(valores1)
        sum_x = sum(valores1)
        sum_y = sum(valores2)
        sum_x2 = sum([valor ** 2 for valor in valores1])
        sum_xy = sum([valores1[i] * valores2[i] for i in range(n)])
        a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
        b = (sum_y - a * sum_x) / n
        return a, b
    
    ## Razones y Proporciones
    def proporciones(self, nombre_columna1, nombre_columna2):
        valores1 = self.obtener_valores_columna(nombre_columna1)
        valores2 = self.obtener_valores_columna(nombre_columna2)
        return sum(valores1) / sum(valores2)
    
    def tasas(self, nombre_columna1, nombre_columna2):
        valores1 = self.obtener_valores_columna(nombre_columna1)
        valores2 = self.obtener_valores_columna(nombre_columna2)
        return sum(valores1) / sum(valores2) * 100
    
    def indices(self, nombre_columna1, nombre_columna2):
        valores1 = self.obtener_valores_columna(nombre_columna1)
        valores2 = self.obtener_valores_columna(nombre_columna2)
        return sum(valores1) / sum(valores2) * 1000
    
    def razon(self, nombre_columna1, nombre_columna2):
        valores1 = self.obtener_valores_columna(nombre_columna1)
        valores2 = self.obtener_valores_columna(nombre_columna2)
        return sum(valores1) / sum(valores2)
    
    def porcentaje_aumentos(self, nombre_columna1, nombre_columna2):
        valores1 = self.obtener_valores_columna(nombre_columna1)
        valores2 = self.obtener_valores_columna(nombre_columna2)
        return (sum(valores1) - sum(valores2)) / sum(valores2) * 100
    
    def porcentaje_disminucion(self, nombre_columna1, nombre_columna2):
        valores1 = self.obtener_valores_columna(nombre_columna1)
        valores2 = self.obtener_valores_columna(nombre_columna2)
        return (sum(valores2) - sum(valores1)) / sum(valores2) * 100
    
    def porcentaje_error(self, nombre_columna1, nombre_columna2):
        valores1 = self.obtener_valores_columna(nombre_columna1)
        valores2 = self.obtener_valores_columna(nombre_columna2)
        return (sum(valores2) - sum(valores1)) / sum(valores2) * 100
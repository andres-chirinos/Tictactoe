from tabla import Tabla

class TablaAgrupada(Tabla):
    def __init__(self, datos:list = None) -> None:
        super().__init__(datos)
        pass

    #Estadisticas
    ## Medidas de Tendencia Central
    def media(self, nombre_columna):
        pass
    
    def mediana(self, nombre_columna):
        pass
    
    def moda(self, nombre_columna):
        pass
    
    ## Medidas de Dispersión
    def desviacion_media(self, nombre_columna):
        pass
    
    def desviacion_mediana(self, nombre_columna):
        pass
    
    def varianza_poblacional(self, nombre_columna):
        pass
    
    def varianza_muestral(self, nombre_columna):
        pass
    
    def rango(self, nombre_columna):
        pass
    
    def rango_cuartilico(self, nombre_columna):
        pass
    
    def rango_semi_cuartilico(self, nombre_columna):
        pass
    
    def coeficiente_varianza(self, nombre_columna):
        pass
    
    def desviacion_tipica_poblacional(self, nombre_columna):
        pass
    
    def desviacion_tipica_muestral(self, nombre_columna):
        pass
    
    ## Medidas de Posición
    def cuartil(self, nombre_columna, q):
        pass
    
    def percentil(self, nombre_columna, p):
        pass
    
    def decil(self, nombre_columna, d):
        pass
    
    ## Medidas de Forma
    def coeficiente_apertura(self, nombre_columna):
        pass
    
    def recorrido_relativo(self, nombre_columna):
        pass
    
    ## Medidas de Relación
    def coeficiente_correlacion(self, nombre_columna1, nombre_columna2):
        pass
    
    def coeficiente_determinacion(self, nombre_columna1, nombre_columna2):
        pass
    
    ## Medidas Especiales
    def media_cuadratica(self, nombre_columna):
        pass
    
    def media_geometrica(self, nombre_columna):
        pass
    
    def media_hiperbolica(self, nombre_columna):
        pass
    
    def recuento_estandar(self, nombre_columna):
        pass
    
    ## Análisis de Regresión
    def regresion_lineal(self, nombre_columna1, nombre_columna2):
        pass

    def regresion_inversa(self, nombre_columna1, nombre_columna2):
        pass

    ## Razones y Proporciones
    def proporciones(self, nombre_columna1, nombre_columna2):
        pass

    def tasas(self, nombre_columna1, nombre_columna2):
        pass

    def indices(self, nombre_columna1, nombre_columna2):
        pass

    def razon(self, nombre_columna1, nombre_columna2):
        pass

    def porcentaje_aumentos(self, nombre_columna1, nombre_columna2):
        pass

    def porcentaje_disminucion(self, nombre_columna1, nombre_columna2):
        pass

    def porcentaje_error(self, nombre_columna1, nombre_columna2):
        pass
    
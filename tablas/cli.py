from tablas import Tabla
from datetime import datetime

if __name__ == "__main__":
    tabla = Tabla()
    tabla.importar_csv("datos/Plantilla.csv")
    # validacion
    tabla.editar_encabezado("item", validado=lambda x: int(x))
    tabla.editar_encabezado(
        "fecha_ing", validado=lambda x: datetime.strptime(x, "%d/%m/%Y")
    )
    tabla.editar_encabezado("nivel_sal", validado=lambda x: int(x))
    tabla.validar()

    # evaluación
    cargos = [None,("Gerente General",18800),("Director", 16650),("Jefe Unidad",14200),("Profesional 1",12000),("Profesional 2",10000),("Administrativo",6500)]
    tabla.agregar_encabezado(
        "cargo",
        evaluado=lambda **registro: cargos[registro["nivel_sal"]][0],
    )
    tabla.agregar_encabezado(
        "sueldo_basico",
        evaluado=lambda **registro: cargos[registro["nivel_sal"]][1],
    )

    antiguedad = [None, 5/100,3.5/100,2/100,None,0]

    def antiguedadf(anios):
        if anios>=10:
            return 1
        if anios>=5:
            return 2
        if anios>=2:
            return 3
        return 5

    tabla.agregar_encabezado(
        "anio",
        evaluado=lambda **registro: (datetime.now()-registro["fecha_ing"]).days//365,
    )
    tabla.agregar_encabezado(
        "mes",
        evaluado=lambda **registro: ((datetime.now()-registro["fecha_ing"]).days-registro["anio"]*365)//(365/12),
    )
    tabla.agregar_encabezado(
        "dia",
        evaluado=lambda **registro: ((datetime.now()-registro["fecha_ing"]).days-registro["anio"]*365-int(registro["mes"]*365/12)),
    )
    tabla.agregar_encabezado(
        "bono_anio",
        evaluado=lambda **registro: antiguedad[antiguedadf(registro["anio"])]*registro["sueldo_basico"],
    )
    tabla.agregar_encabezado(
        "bono_ant",
        evaluado=lambda **registro: registro["bono_anio"]*registro["anio"],
    )
    tabla.agregar_encabezado(
        "total_ingreso",
        evaluado=lambda **registro: registro["bono_ant"]+registro["sueldo_basico"],
    )
    minimo_nacional = 2500
    tabla.agregar_encabezado(
        "iva",
        evaluado=lambda **registro: registro["total_ingreso"]*(13/100) if registro["total_ingreso"]>=4*minimo_nacional else 0,
    )
    tabla.agregar_encabezado(
        "afp",
        evaluado=lambda **registro: registro["total_ingreso"]*(1271/10000),
    )
    tabla.agregar_encabezado(
        "total_descuentos",
        evaluado=lambda **registro: registro["iva"]+registro["afp"],
    )
    tabla.agregar_encabezado(
        "facturas",
        evaluado=lambda **registro: registro["total_ingreso"]-4*minimo_nacional if registro["iva"]!=0 else 0 ,
    )
    tabla.agregar_encabezado(
        "liquido_pagable",
        evaluado=lambda **registro: registro["total_ingreso"]-registro["total_descuentos"],
    )
    tabla.calcular()
    tabla.mostrar_tabla()
    tabla.exportar_tabla("datos/Plantilla2.csv")
    """
    # evalucion
    def anios(fecha_de_ingreso):
        tiempo = datetime.now() - fecha_de_ingreso
        return tiempo.days // 365

    tabla.agregar_encabezado(
        "anio_de_trabajo",
        evaluado=lambda **registro: anios(registro["fecha_de_ingreso"]),
    )

    def clasificar(anios):
        if anios > 1 and anios <= 4:
            return "D"
        if anios > 4 and anios <= 8:
            return "C"
        if anios > 8 and anios <= 13:
            return "B"
        if anios > 13:
            return "A"
        return None

    tabla.agregar_encabezado(
        "anio_de_trabajo_categoria",
        evaluado=lambda **registro: clasificar(registro["anio_de_trabajo"]),
    )
    tabla.agregar_encabezado(
        "bono_movilidad",
        evaluado=lambda **registro: (
            200 if registro["cargo"].lower() == "mensajero" else 0
        ),
    )

    def clasificar_categoria(categoria, haber_basico):
        categoria = categoria.lower()
        if categoria == "a" or categoria == "b":
            return haber_basico * 0.1
        if categoria == "c" or categoria == "d":
            return haber_basico * 0.07
        return 0

    tabla.agregar_encabezado(
        "bono_extra",
        evaluado=lambda **registro: clasificar_categoria(
            registro["anio_de_trabajo_categoria"], registro["haber_cargo"]
        ),
    )

    def clasificar_antiguedad(antiguedad, haber_basico, anios):
        antiguedad = antiguedad.lower()
        if antiguedad == "a":
            return haber_basico * 0.035 * anios
        if antiguedad == "b":
            return haber_basico * 0.03 * anios
        if antiguedad == "c":
            return haber_basico * 0.027 * anios
        if antiguedad == "d":
            return haber_basico * 0.022 * anios
        return 0

    tabla.agregar_encabezado(
        "bono_antiguedad",
        evaluado=lambda **registro: clasificar_antiguedad(
            registro["anio_de_trabajo_categoria"],
            registro["haber_cargo"],
            registro["anio_de_trabajo"],
        ),
    )
    tabla.agregar_encabezado(
        "total_ganado",
        evaluado=lambda **registro: registro["haber_cargo"]
        + registro["bono_movilidad"]
        + registro["bono_extra"]
        + registro["bono_antiguedad"],
    )
    tabla.agregar_encabezado(
        "descuento_iva",
        evaluado=lambda **registro: (
            registro["total_ganado"] * 0.13 if registro["total_ganado"] >= 3000 else 0
        ),
    )
    tabla.agregar_encabezado(
        "descuento_afp", evaluado=lambda **registro: registro["total_ganado"] * 0.055
    )
    tabla.agregar_encabezado(
        "descuento_club",
        evaluado=lambda **registro: 200 if registro["haber_cargo"] >= 2000 else 0,
    )
    tabla.agregar_encabezado(
        "total_descuentos",
        evaluado=lambda **registro: registro["descuento_iva"]
        + registro["descuento_afp"]
        + registro["descuento_club"],
    )
    tabla.agregar_encabezado(
        "liquido_pagable",
        evaluado=lambda **registro: registro["total_ganado"]
        - registro["total_descuentos"],
    )
    """

from datetime import date, timedelta


def es_bisiesto(anio: int) -> bool:
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)


def obtener_dias_del_mes(mes: int, anio: int) -> int:
    # Abril, junio, septiembre y noviembre tienen 30
    if mes in [4, 6, 9, 11]:
        return 30
    # Febrero depende de si es o no bisiesto
    if mes == 2:
        if es_bisiesto(anio):
            return 29
        else:
            return 28
    else:
        # En caso contrario, tiene 31 días
        return 31


def obtener_fechas(month, year):

    dias = obtener_dias_del_mes(month, year)

    start = date(year, month, 1)

    all_days = (start + timedelta(x) for x in range((dias)))

    return all_days

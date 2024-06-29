"""
Desarrolla un programa que calcule la cantidad de días hábiles entre dos fechas ingresadas por el usuario, 
excluyendo fines de semana y días festivos.
"""

import holidays_co
import datetime


def Calculo_dias_Habiles(Fecha_inicial,Fecha_Final):
    feriados = set()
    for year in range(Fecha_inicial.year, Fecha_Final.year + 1):
        feriados.update(holidays_co.get_colombia_holidays_by_year(year))
    feriados = {feriado.date for feriado in feriados}

    cantidad = (Fecha_Final-Fecha_inicial).days
    for i in range(1, cantidad + 1):
        if (Fecha_inicial + datetime.timedelta(i)).weekday() >= 5:
            cantidad -= 1
        elif (Fecha_inicial + datetime.timedelta(i)) in feriados:
            cantidad -=1
    return cantidad

"""--------------------------------Segunda forma -----------------------------------------------------------"""
def calcular_dias_habiles(inicio: datetime, fin: datetime) -> int:
    feriados = set()
    for year in range(inicio.year, fin.year + 1):
        feriados.update(holidays_co.get_colombia_holidays_by_year(year))
    feriados = {feriado.date for feriado in feriados}
    dias_totales = (fin - inicio).days + 1
    dias_feriados = sum(1 for fecha in range(int((fin - inicio).days) + 1) if inicio+datetime.timedelta(fecha) in feriados)
    dias_fines_de_semana = sum(1 for fecha in range(int((fin - inicio).days) + 1) if (inicio+datetime.timedelta(fecha)).weekday() >= 5)
    dias_habiles = dias_totales - dias_feriados - dias_fines_de_semana
    return dias_habiles            

# BLOQUE DE DEFINICIÓN
# IMPORTACION DE FUNCIONES
import os
import sys
import json
import calendar
import requests
import re
from datetime import date
import numpy as np
import matplotlib.pyplot as plt


def Clean():
    os.system("cls")


def Exit():
    sys.exit


def DiasFeriados():
    Clean()
    response = requests.get('https://www.feriadosapp.com/api/holidays.json')
    packages_json = response.json()
    i = 0
    date = []
    while i < len(packages_json['data']):
        date.append(packages_json['data'][i]['date'])
        i += 1
    j = 0
    temp_date = ''
    current_month = [['Enero'], ['Febrero'], ['Marzo'], [
                    'Abril'], ['Mayo'], ['Junio'], ['Julio'], ['Agosto'], [
                    'Septiembre'], ['Octubre'], ['Noviembre'], ['Diciembre']]
    while j < len(date):
        temp_date = date[j].split('-')
        if int(temp_date[0]) == current_year:
            current_month[(int(temp_date[1]) - 1)].append(temp_date[2])
        else:
            j += 1
        j += 1
    k = 0
    while k < len(current_month):
        if len(current_month[k]) > 1:
            l = 1
            current_days = ''
            while l < len(current_month[k]):
                current_days = current_days + str((current_month[k][l])) + ' '
                l += 1
            print('En ', current_month[k][0],
                  'seran feriado los siguientes dias: ', current_days)
        else:
            k += 1
        k += 1
    Consulta()


def VerCalendario():
    Clean()
    condition = int(input('Deseas ver el año entero o un mes en especifico? '))
    if condition == 1:
        Clean()
        print(calendar.calendar(current_year))
        Consulta()
    elif condition == 2:
        Clean()
        month = int(input('Que mes quieres visualizar? (1 al 12)'))
        if month <= 12:
            Clean()
            print(calendar.month(current_year, month))
            Consulta()
        else:
            Clean()
            print(Error404)
            VerCalendario()
    else:
        Clean()
        print(Error404)
        VerCalendario()


def Consulta():
    temp = input('¿Deseas volver al Menu principal? (1 (Si) /2 (No)) ')
    if temp == '1':
        Clean()
        Menu()
    elif temp == '2':
        Clean()
        Exit()
    else:
        Clean()
        print('Ups parace que te haz equivocado')
        Consulta()


def Menu():
    Clean()
    print('''(1)  Visualizar dias feriados del Año
             \r(2)  Ver Calendario
             \r(3)  Calculadora
             \r(4)  Ver grafico
             \r(5)  Exit''')
    temp = input('Que opcion deseas? ')
    if temp == "1":
        DiasFeriados()
    elif temp == "2":
        VerCalendario()
    elif temp == "3":
        Calculadora()
    elif temp == "4":
        Grafico()
    elif temp == "5":
        Clean()
        print('Adios')
        Exit()
    else:
        Clean()
        print('Ups parace que te haz equivocado')
        Consulta()


def Convert(nombre_archivo):
    archivo = open(nombre_archivo, 'r')
    lineas = archivo.readlines()
    archivo.close()
    stri = ''.join(lineas)
    stri = stri.split('\n')
    i = 0
    temp = []
    while i < len(stri):
        temp.append(stri[i])
        i += 1
    j = 0
    temp2 = []
    while j < len(temp):
        temp2.append(temp[j].split(','))
        j += 1
    return temp2


def Calculadora():
    valores = []
    nombres = []
    i = 0
    while i < len(viajes):
        temp_month = calendar.month(current_year, i + 1)
        dias = []
        j = 1
        while j < len(viajes[i]):
            dias.append(viajes[i][j])
            j += 1
        Pos = []
        Nmbr = []
        for r in re.finditer('\d+', temp_month):
            Nmbr.append(r.group(0))
            Pos.append(r.start())
        Nmbr.pop(0)
        Pos.pop(0)
        k = 0
        while k < len(dias):
            l = 0
            while l < len(Nmbr):
                if Nmbr[l] == dias[k]:
                    temp_month_list = list(temp_month)
                    if len(dias[k]) == 1:
                        temp_month_list[int(Pos[l])] = 'X'
                        temp_month = ''.join(temp_month_list)
                    elif len(dias[k]) == 2:
                        temp_month_list[int(Pos[l])] = ' '
                        temp_month_list[int(Pos[l]) + 1] = 'X'
                        temp_month = ''.join(temp_month_list)
                    else:
                        l += 1
                l += 1
            k += 1
        print(temp_month)
        valores.append(Gastos(temp_month))
        nombres.append(viajes[i][0])
        i += 1
    Database(nombres, valores)
    Consulta()


def Gastos(mes):
    value = 0
    for letra in mes:
        if letra == 'X':
            value = value + costo_pasaje
    print('En este mes gastaras : %s pesos' % (value))
    return value


def Database(nombre, value):
    archivo = open('Database.txt', 'w')
    i = 0
    while i < len(nombre):
        if i == len(nombre) - 1:
            inside = nombre[i] + ' ' + str(value[i])
        else:
            inside = nombre[i] + ' ' + str(value[i]) + '\n'
        archivo.write(inside)
        i += 1
    archivo.close()


def Grafico():
    archivo = open('Database.txt', 'r')
    lineas = archivo.readlines()
    archivo.close()
    stri = ''.join(lineas)
    stri = stri.split('\n')
    temp = []
    etiquetas = []
    valores = []
    i = 0
    while i < len(stri):
        temp.append(stri[i].split(' '))
        etiquetas.append(temp[i][0])
        valores.append(int(temp[i][1]))
        i += 1
    print(etiquetas)
    print(valores)
    posiciones = np.arange(len(etiquetas))
    plt.bar(posiciones, valores, alpha=1.0, width=0.5)
    plt.xticks(posiciones, etiquetas)
    plt.ylabel('Gatos $ (en clp)')
    plt.title('Gastos segun cada mes en pasajes')
    plt.show()
    # Consulta()


# BLOQUE PRINCIPAL
# EL PROGRAMA NO TIENE ENTRADA, PUES LA FUNCION ESTA PREDEFINIDA
viajes = Convert('Viajes.txt')
Error404 = 'Ups.. Parece que te haz equivocado, vamos a intentarlo de nuevo. '
calendario = []
costo_pasaje = 350
current_year = 2020  # date.today().year
# De momento ninguna API de feriados en chile posee una actualizacion para el
# 2020, por esto, la simulacion sera en el año anterior
if __name__ == '__main__':
    Menu()
# EL PROGRAMA NO TIENE SALIDA, PUES LA FUNCION ESTA PREDEFINIDA

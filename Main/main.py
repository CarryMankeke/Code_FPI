import os
import sys
import json
import calendar
import requests
import re
from datetime import date
Error404 = 'Ups.. Parece que te haz equivocado, vamos a intentarlo de nuevo. '
calendario = []
current_year = date.today().year


def Clean():
    os.system("cls")


def Menu():
    Clean()
    print('(1)  Obtener Dias feriados del Año')
    print('(2)  Ver Calendario')
    print('(3)  Modificar Dias')
    print('(4)  Salir')
    temp = input('Que opcion deseas? ')
    if temp == "1":
        DiasFeriados()
    elif temp == "2":
        VerCalendario()
    elif temp == "3":
        ModificarDias()
    elif temp == "4":
        Clean()
        print('Adios')
        salir()
    else:
        Clean()
        print('Ups parace que te haz equivocado')
        Consulta()


def DiasFeriados():
    Clean()
    response = requests.get('https://www.feriadosapp.com/api/holidays.json')
    packages_json = response.json()
    i = 0
    date = []
    while i < len(packages_json['data']):
        date.append(packages_json['data'][i]['date'])
        i += 1
    Clean()
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
    condition = int(input('Quieres ver el año entero o un mes en especifico?'))
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


def ModificarDias():
    Clean()
    print(calendar.calendar(current_year))
    month = int(input('Ingresa un mes (1 al 12) '))
    Clean()
    if month <= 12:
        temp_month = calendar.month(current_year, month)
        print(temp_month)
        entry = input('Ingresa los dias que viajaras separados por un espacio')
        entry = entry.split(' ')
        Clean()
        Pos = []
        Nmbr = []
        for r in re.finditer('\d+', temp_month):
            Nmbr.append(r.group(0))
            Pos.append(r.start())
        Nmbr.pop(0)
        Pos.pop(0)
        i = 0
        while i < len(entry):
            j = 0
            while j < len(Nmbr):
                if Nmbr[j] == entry[i]:
                    temp_month_list = list(temp_month)
                    if  len(entry[i]) == 1:
                        temp_month_list[int(Pos[j])] = 'X'
                        temp_month = ''.join(temp_month_list)
                    elif len(entry[i]) == 2:
                        temp_month_list[int(Pos[j])] = ' '
                        temp_month_list[int(Pos[j]) + 1] = 'X'
                        temp_month = ''.join(temp_month_list)
                    else:
                        j += 1
                j += 1
            i += 1
        print(temp_month)
        Consulta()
    else:
        print(Error404)
        ModificarDias()


def salir():
    sys.exit


def Consulta():
    temp = input('¿Deseas volver al Menu principal? (1 (Si) /2 (No)) ')
    if temp == '1':
        Clean()
        Menu()
    elif temp == '2':
        Clean()
        salir()
    else:
        Clean()
        print('Ups parace que te haz equivocado')
        Consulta()


Menu()

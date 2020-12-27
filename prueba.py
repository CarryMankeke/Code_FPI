import calendar
import os
import re
current_year = 2020
Error404 = 'Te haz equivocado'


def Clean():
    os.system("cls")


def ModificarDias():
    Clean()
    print(calendar.calendar(current_year))
    # month = int(input('Ingresa un mes (1 al 12) '))
    month = 5   # Recordar cambiar
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
                    temp_month_list[int(Pos[j])] = 'X'
                    temp_month = ''.join(temp_month_list)
                j += 1
            i += 1
        print(temp_month)
    else:
        print(Error404)
        ModificarDias()

ModificarDias()

import calendar
import os
current_year = 2020
Error404 = 'Te haz equivocado'


def Clean():
    os.system("cls")


def ModificarDias():
    Clean()
    print(calendar.calendar(current_year))
    # month = int(input('Ingresa un mes (1 al 12) '))
    month = 5
    Clean()
    if month <= 12:
        temp_month = calendar.month(current_year, month)
        print(temp_month)
        entry = input('Ingresa los dias que viajaras separados por un espacio')
        entry = entry.split(' ')
        Clean()
        j = 0
        while j < len(entry):
            i = 25
            while i < len(temp_month):
                if (i + 1) < len(temp_month):
                    if temp_month[i] + temp_month[i + 1] == str(entry[j]):
                        temp_month_list = list(temp_month)
                        temp_month_list[i] = " "
                        temp_month_list[i + 1] = "X"
                        temp_month = "".join(temp_month_list)
                        print('A')
                        print(entry[j])
                        i += len(temp_month) - 1
                    elif temp_month[i] == str(entry[j]) and temp_month[i + 1] == ' ' :
                        temp_month_list = list(temp_month)
                        temp_month_list[i] = "X"
                        temp_month = "".join(temp_month_list)
                        print('B')
                        print(entry[j])
                        print(temp_month[i])
                        i += len(temp_month) - 1
                    else:
                        i += 1
                else:
                    if temp_month[i] == str(entry[j]) and temp_month[i - 1] == ' ' :
                        temp_month_list = list(temp_month)
                        temp_month_list[i] = "X"
                        temp_month = "".join(temp_month_list)
                        print('C')
                        print(entry[j])
                        i += len(temp_month) - 1
                    else:
                        i += 1
                i += 1
            j += 1
        print(entry)
        print(temp_month)
    else:
        print(Error404)
        ModificarDias()

ModificarDias()

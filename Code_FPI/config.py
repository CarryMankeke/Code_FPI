import os
import sys
import json
import calendar
import requests
Error404 = 'Ups.. Parece que te haz equivocado, vamos a intentarlo de nuevo. '

def DiasFeriados():
    response = requests.get('https://www.feriadosapp.com/api/holidays.json')
    packages_json = response.json()
    i = 0
    date = []
    while i < len(packages_json['data']):
        date.append(packages_json['data'][i]['date'])
        i += 1
    j = 0
    temp_date = ''
    current_month = [[], [], [], [], [], [], [], [], [], [], [], []]
    while j < len(date):
        temp_date = date[j].split('-')
        if int(temp_date[0]) == current_year:
            current_month[(int(temp_date[2])- 1)].append(temp_date[3])
        else:
            j += 1
        j += 1
    print(current_month)
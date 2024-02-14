import requests
import sys
import time
from analice_file import analice_items
from obtener_fechas import obtener_fechas


if len(sys.argv) == 3:
    MONTH = sys.argv[1]
    YEAR = sys.argv[2]
else:
    print("faltan parámetros")
    sys.exit(1)

print(f'A Procesar -> Mes: {MONTH} - Año: {YEAR}')

url = 'https://api.botmaker.com/v2.0/sessions'

headers = {'access-token': 'eyJhbGciOiJIUzUxMiJ9.eyJidXNpbmVzc0lkIjoiZ3Vyd' +
           'SIsIm5hbWUiOiJEZWx1Y2EgR2VyYXJkbyBBcmllbCAoQVIpIiwiYXBpIjp0cnV' +
           'lLCJpZCI6InJVRVd0QXdGZmZVTThxdDhuOXF5TE41RlBnMzIiLCJleHAiOjE4M' +
           'zY0OTcyNjQsImp0aSI6InJVRVd0QXdGZmZVTThxdDhuOXF5TE41RlBnMzIifQ.' +
           'SsEkxqP6t0rb5P_C6_zNxudavX-Nb-Ex85c1t6v71KChnpFMTz1iqJyYj6xc1k' +
           'K3Jhq0iP7e3dmpUy4Kte6zfg'
           }


def get_message(desde, hasta, archivo):

    params = {'from': desde,
              'include-events': True,
              'include-messages': True,
              'include-open-sessions': True,
              'include-variables': False,
              'long-term-search': True,
              'to': hasta
              }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        CSV = []

        # Header del csv
        cadena = ('id;chatId;channelId;contactId;from\n')

        CSV.append(cadena)
        iTerar = '1'
        ii = 0

        while iTerar == '1' and response.status_code == 200:
            datos = response.json()
            datos_log = response.text
            ii += 1
            log = 'response_' + dia + "_" + str(ii) + '.json'
            with open(log, 'w',  encoding="utf8") as archivo:
                archivo.write(datos_log)
            analice_items(CSV, datos)
            nextPage = datos['nextPage']
            if nextPage:
                print('nxtPage')
                response = requests.get(nextPage, headers=headers)
            else:
                iTerar = '0'

        strCSV = "".join(CSV)
        with open(archivo, 'w',  encoding="utf8") as archivo:
            archivo.write(strCSV)
    else:
        print(f'Status: {response.status_code}')

    return response.status_code


mes = int(MONTH)
anio = int(YEAR)
dias_a_procesar = obtener_fechas(mes, anio)

for day in dias_a_procesar:
    dia = day.strftime('%Y-%m-%d')
    desde = dia + 'T06:00:00.000Z'
    hasta = dia + 'T23:00:00.000Z'
    archivo = 'chat_' + dia + '.csv'
    print('desde: {} -  hasta: {} - archivo: {}'.format(desde, hasta, archivo))
    iError = get_message(desde, hasta, archivo)
    if iError != 200:
        sys.exit(1)
    time.sleep(5)
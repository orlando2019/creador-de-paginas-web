import time
from datetime import datetime as dt

hosts_path_windows = r"C:\Windows\System32\drivers\etc\hosts"
#hosts_temporal = "hosts"
hosts_temporal = hosts_path_windows
redirect = "127.0.0.1"

lista_website = [
    "www.facebook.com",
    "facebook.com",
    "",
    "",
    "https://web.facebook.com/?_rdc=1&_rdr",
    "www.pornogratisdiario.com",
    "",
    ""
]

from_hour = 6
to_hour = 23
dt_from = dt(dt.now().year, dt.now().month, dt.now().day, from_hour)
dt_to = dt(dt.now().year, dt.now().month, dt.now().day, to_hour)

while True:
    if dt_from < dt.now() < dt_to:
        print("Working...")
        with open(hosts_temporal, 'r+') as file:
            content = file.read()
            for website in lista_website:
                if website in content:
                    pass
                else:
                    file.write(redirect + ' ' + website + '\n')

    else:
        print("Estoy Viendo Facebook...")
        with open(hosts_temporal, 'r+') as file:
            content = file.readlines()
            file.seek(0)  # Aqui nos ubicamos siempre en la primera linea
            # En este  for recorremos content y comprobamos que el sitio este en la linea del archivo hosts
            for line in content:
                if not any(website in line for website in lista_website):
                    file.write(line)
            file.truncate()
    time.sleep(1)

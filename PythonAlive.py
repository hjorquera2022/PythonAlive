import os
import socket

# Función para obtener el estado de la dirección IP
def get_status(ip):
    try:
        # Intenta conectarse al puerto 80 de la dirección IP
        socket.create_connection((ip, 80), timeout=1)
        return "VERDE"
    except:
        # Si no se puede conectar, intenta hacer ping a la dirección IP
        response = os.system("ping -c 1 " + ip)
        if response == 0:
            return "AMARILLO"
        else:
            return "ROJO"


# Abrimos el archivo de entrada en modo lectura
with open('C:\\Users\\hjorquera\\Desktop\\advanced_ip_scanner_console\\archivo_entrada.txt', 'r', encoding='utf-8') as archivo_entrada:

    # Abrimos el archivo de salida en modo escritura
    with open('C:\\Users\\hjorquera\\Desktop\\advanced_ip_scanner_console\\archivo_alive.txt', 'w', encoding='utf-8') as archivo_salida:

        # Escribimos el encabezado en el archivo de salida
        linea = 'Status | Name | Type | Operating system | IP | NetBIOS name | NetBIOS group | Manufacturer | MAC address | User\n'
        archivo_salida.write(linea.replace('|', ','))

        # Iteramos sobre cada línea del archivo de entrada
        for linea in archivo_entrada:

            # Si la línea contiene la palabra clave "alive", la escribimos en el archivo de salida
            if 'alive' in linea:
                archivo_salida.write(linea.replace('|', ','))

# Abrimos el archivo de entrada en modo lectura
with open('C:\\Users\\hjorquera\\Desktop\\advanced_ip_scanner_console\\archivo_alive.txt', 'r', encoding='utf-8') as archivo_entrada:

    # Abrimos el segundo archivo de salida en modo escritura
    with open('C:\\Users\\hjorquera\\Desktop\\advanced_ip_scanner_console\\archivo_salida.txt', 'w', encoding='utf-8') as archivo_salida:

        # Escribimos el encabezado en el archivo de salida
        linea = ' IP , Name ,User \n'
        archivo_salida.write(linea)

        # Iteramos sobre cada línea del archivo de entrada
        for linea in archivo_entrada:

            # Si la línea contiene la palabra clave "alive", escribimos la dirección IP en el archivo de salida
            if 'alive' in linea:
                campos = linea.strip().split(',')

                if campos[4] == '':
                   campos[4] = 'SIN-IP'
                if campos[1] == '':
                   campos[1] = 'SIN-NOMBRE'
                if campos[9] == '':
                   campos[9] = 'SIN-USER'

                archivo_salida.write(campos[4] + ',' + campos[1] + ',' + campos[9] +'\n')



# Paso 1: Leer el archivo de texto y almacenar los datos en una lista
data = []
with open('C:\\Users\\hjorquera\\Desktop\\advanced_ip_scanner_console\\archivo_salida.txt', 'r', encoding='utf-8') as f:
    # Leer la primera línea y descartarla
    header = f.readline()
    # Leer las líneas restantes y almacenar los datos en una lista
    for line in f:
        ip, nombre, usuario = line.strip().split(',')
        data.append((ip, nombre, usuario))

# Paso 2: Crear un diccionario vacío para almacenar el estado de cada IP
estado = {}

# Paso 3: Recorrer la lista de datos y para cada IP, realizar una prueba de conexión y actualizar el diccionario de estado
for ip, nombre, usuario in data:
     # Obtención del estado de la dirección IP
     estado[ip] = get_status(ip)

# Paso 4: Presentar el tablero de control con los estados de las IPs
print('IP\tEstado')
for ip, estado_ip in estado.items():
    print(f'{ip} \t{estado_ip} ')
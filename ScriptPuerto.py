import socket #Importa la libreria Socket

target = input("Introduce la IP o dominio: ")#Linea para que el usuario inserte la direccion IP a escanear
with open("scan_results.txt", "w") as file:#Abre un archivo .txt para guardar los resultados
    for port in range(1, 65535):#Recorre todos los puertos en un rango
        print(f"Escaneando puerto {port}...")#Muestra en pantalla los puertos que estan siendo escaneados
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:#Creara un Socket
            s.settimeout(1)#Este comando permite establecer cada cuanto tiempo se realizará el escaneo
            if s.connect_ex((target, port)) == 0:#Intetara conectarse al puerto especificado 
                print(f"Puerto {port} abierto")#Si el puerto se encuetra abierto aparecera "Puerto Abierto"
                file.write(f"Puerto {port} abierto\n")#Guarda el resultado en el archivo .txt
            else:#De lo contrario
                print(f"Puerto {port} cerrado")#Aparecerá "Puerto Cerrado"
print("Resultados guardados en scan_results.txt")#Los resultados se guardaran en un .txt 

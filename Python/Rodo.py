import os
import shutil

# Ruta de la carpeta de origen (donde están las carpetas con archivos)
ruta_origen = r'C:\Users\Tomás L\Desktop\Rodo'

# Ruta de la carpeta de destino
ruta_destino = r'C:\Users\Tomás L\Desktop\Todo'

# Verificar si las rutas existen
if not os.path.exists(ruta_origen):
    print(f"Error: La ruta de origen {ruta_origen} no existe.")
else:
    print(f"La ruta de origen {ruta_origen} existe.")

if not os.path.exists(ruta_destino):
    print(f"Error: La ruta de destino {ruta_destino} no existe. Creando carpeta de destino.")
    os.makedirs(ruta_destino, exist_ok=True)
else:
    print(f"La ruta de destino {ruta_destino} existe.")

# Función para mover archivos de subcarpetas a la carpeta de destino
def mover_archivos_de_subcarpetas(ruta_origen, ruta_destino):
    print(f"Ruta de origen: {ruta_origen}")
    print(f"Ruta de destino: {ruta_destino}")
    for root, dirs, files in os.walk(ruta_origen):
        print(f"Revisando directorio: {root}")
        for archivo in files:
            if archivo.lower().endswith('.pdf'):
                archivo_origen = os.path.join(root, archivo)
                destino = os.path.join(ruta_destino, archivo)
                
                # Verificar si el archivo de origen existe
                if not os.path.exists(archivo_origen):
                    print(f"Error: El archivo de origen {archivo_origen} no existe.")
                    continue
                
                # Verificar si un archivo con el mismo nombre ya existe en la carpeta de destino
                if os.path.exists(destino):
                    base, extension = os.path.splitext(archivo)
                    i = 1
                    nuevo_destino = os.path.join(ruta_destino, f"{base}_{i}{extension}")
                    while os.path.exists(nuevo_destino):
                        i += 1
                        nuevo_destino = os.path.join(ruta_destino, f"{base}_{i}{extension}")
                    destino = nuevo_destino
                
                try:
                    print(f"Moviendo archivo: {archivo_origen} a {destino}")
                    shutil.move(archivo_origen, destino)
                except FileNotFoundError as e:
                    print(f"Error al mover {archivo_origen} a {destino}: {e}")
                except Exception as e:
                    print(f"Ocurrió un error inesperado al mover {archivo_origen} a {destino}: {e}")

# Llamar a la función para mover archivos si las rutas existen
if os.path.exists(ruta_origen) and os.path.exists(ruta_destino):
    mover_archivos_de_subcarpetas(ruta_origen, ruta_destino)

print("Proceso completado.")


# Función para mover archivos de subcarpetas a la carpeta de destino
def mover_archivos_de_subcarpetas(ruta_origen, ruta_destino):
    print(f"Ruta de origen: {ruta_origen}")
    print(f"Ruta de destino: {ruta_destino}")
    for root, dirs, files in os.walk(ruta_origen):
        print(f"Revisando directorio: {root}")
        for archivo in files:
            if archivo.lower().endswith('.pdf'):
                archivo_origen = os.path.join(root, archivo)
                destino = os.path.join(ruta_destino, archivo)
                
                # Verificar si un archivo con el mismo nombre ya existe en la carpeta de destino
                if os.path.exists(destino):
                    base, extension = os.path.splitext(archivo)
                    i = 1
                    nuevo_destino = os.path.join(ruta_destino, f"{base}_{i}{extension}")
                    while os.path.exists(nuevo_destino):
                        i += 1
                        nuevo_destino = os.path.join(ruta_destino, f"{base}_{i}{extension}")
                    destino = nuevo_destino
                
                try:
                    print(f"Moviendo archivo: {archivo_origen} a {destino}")
                    shutil.move(archivo_origen, destino)
                except FileNotFoundError as e:
                    print(f"Error al mover {archivo_origen} a {destino}: {e}")
                except Exception as e:
                    print(f"Ocurrió un error inesperado al mover {archivo_origen} a {destino}: {e}")

# Llamar a la función para mover archivos si las rutas existen
if os.path.exists(ruta_origen) and os.path.exists(ruta_destino):
    mover_archivos_de_subcarpetas(ruta_origen, ruta_destino)

print("Proceso completado.")
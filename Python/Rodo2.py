import os
import shutil

# Ruta de la carpeta que contiene los archivos
ruta_carpeta = r'C:\Users\Tomás L\Desktop\Todo'

# Verificar si la ruta existe
if not os.path.exists(ruta_carpeta):
    print(f"Error: La ruta {ruta_carpeta} no existe.")
else:
    print(f"La ruta {ruta_carpeta} existe.")

# Función para ordenar archivos según las secciones en sus nombres
def ordenar_archivos_por_seccion(ruta_carpeta):
    for archivo in os.listdir(ruta_carpeta):
        if archivo.lower().endswith('.pdf'):
            # Obtener la sección del nombre del archivo (suponiendo que está antes de un guion bajo '_')
            seccion = archivo.split('_')[0]
            carpeta_seccion = os.path.join(ruta_carpeta, seccion)
            
            # Crear la carpeta de la sección si no existe
            if not os.path.exists(carpeta_seccion):
                os.makedirs(carpeta_seccion)
            
            archivo_origen = os.path.join(ruta_carpeta, archivo)
            archivo_destino = os.path.join(carpeta_seccion, archivo)
            
            # Verificar si un archivo con el mismo nombre ya existe en la carpeta de destino
            if os.path.exists(archivo_destino):
                base, extension = os.path.splitext(archivo)
                i = 1
                nuevo_destino = os.path.join(carpeta_seccion, f"{base}_{i}{extension}")
                while os.path.exists(nuevo_destino):
                    i += 1
                    nuevo_destino = os.path.join(carpeta_seccion, f"{base}_{i}{extension}")
                archivo_destino = nuevo_destino
            
            # Mover el archivo a la carpeta de la sección correspondiente
            try:
                print(f"Moviendo archivo: {archivo_origen} a {archivo_destino}")
                shutil.move(archivo_origen, archivo_destino)
            except FileNotFoundError as e:
                print(f"Error al mover {archivo_origen} a {archivo_destino}: {e}")
            except Exception as e:
                print(f"Ocurrió un error inesperado al mover {archivo_origen} a {archivo_destino}: {e}")

# Llamar a la función para ordenar los archivos si la ruta existe
if os.path.exists(ruta_carpeta):
    ordenar_archivos_por_seccion(ruta_carpeta)

print("Proceso completado.")

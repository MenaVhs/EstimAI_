import csv
import tkinter as tk
from tkinter import filedialog
import datetime
import os
from PoseClassification.saveCentroind import save_centroids_txt



def import_distance_contition_to_CSV(datos, unit, joint, event_time, condition, video_path, FPS, NY):
    # Crear una instancia de Tkinter
    root = tk.Tk()
    root.withdraw()
    n = 0

    # Obtener la fecha actual y formatearla como una cadena con el formato deseado
    fecha_actual = datetime.datetime.now().strftime('%Y-%m-%d')
    # Establecer el nombre de archivo predeterminado como la fecha de creación del archivo
    nombre_archivo = f'{joint}_{fecha_actual}.csv'

    # Pedir al usuario que seleccione la ubicación y el nombre del archivo
    ruta_archivo = filedialog.asksaveasfilename(defaultextension='.csv', filetypes=[('CSV', '*.csv')],
                                                initialfile=nombre_archivo)

    # Verificar si la ruta del archivo ya existe y agregar un número entre paréntesis al final del nombre de archivo si es necesario
    while os.path.exists(ruta_archivo):
        ruta_sin_extension, extension = os.path.splitext(ruta_archivo)
        ruta_base = os.path.basename(ruta_sin_extension)
        partes_ruta_base = ruta_base.split('(')
        if len(partes_ruta_base) > 1:
            num_str = partes_ruta_base[-1].split(')')[0]
            if num_str.isdigit():
                n = int(num_str)
        ruta_base = f'{ruta_base.split("(")[0]}({n + 1})'
        ruta_archivo = os.path.join(os.path.dirname(ruta_archivo), f'{ruta_base}{extension}')

    while ruta_archivo == '':
        ruta_archivo = filedialog.asksaveasfilename(defaultextension='.csv', filetypes=[('CSV', '*.csv')],
                                                    initialfile=nombre_archivo)

        # Verificar si la ruta del archivo ya existe y agregar un número entre paréntesis al final del nombre de archivo si es necesario
        while os.path.exists(ruta_archivo):
            ruta_sin_extension, extension = os.path.splitext(ruta_archivo)
            ruta_base = os.path.basename(ruta_sin_extension)
            partes_ruta_base = ruta_base.split('(')
            if len(partes_ruta_base) > 1:
                num_str = partes_ruta_base[-1].split(')')[0]
                if num_str.isdigit():
                    n = int(num_str)
            ruta_base = f'{ruta_base.split("(")[0]}({n + 1})'
            ruta_archivo = os.path.join(os.path.dirname(ruta_archivo), f'{ruta_base}{extension}')

    # Abrir el archivo en modo de escritura
    with open(ruta_archivo, mode='w', newline='') as archivo_csv:
        # Crear un objeto csv.writer utilizando el archivo abierto
        escritor_csv = csv.writer(archivo_csv, delimiter=',')

        escritor_csv.writerow(['Joint tracked:', joint])
        escritor_csv.writerow(['Event time:', event_time, 'sec'])
        escritor_csv.writerow(['Condition:', condition, unit])
        escritor_csv.writerow(['Video Path:', video_path])
        escritor_csv.writerow(['FPS', FPS])
        escritor_csv.writerow([])

        # Escribir los headers en el archivo
        headers = ["Sample no.", "Time", 'X', 'Y', f'Frame Dist ({unit})', f'Tot Dist ({unit})',
                   f'Event1 Acc Dist ({unit}) ', 'Event 1']
        escritor_csv.writerow(headers)

        for i in range(len(datos[0])):
            fila = [i] + [datos[j][i] for j in range(len(datos))]
            escritor_csv.writerow(fila)

    # Cerrar el archivo
    archivo_csv.close()


def import_clusters(data_frame, centroids):
    # Abrir una ventana modal para seleccionar el archivo de salida
    root = tk.Tk()
    root.withdraw()

    filename = 'dataset_with_clustering.csv'
    file_path = filedialog.asksaveasfilename(initialfile=filename, defaultextension='.csv', filetypes=[('CSV Files', '*.csv')])

    if file_path:
        file_exists = os.path.exists(file_path)
        if file_exists:
            n = 1
            path_without_ext, ext = os.path.splitext(file_path)
            new_path = f'{path_without_ext} ({n}){ext}'
            while os.path.exists(new_path):
                n += 1
                new_path = f'{path_without_ext} ({n}){ext}'
            file_path = new_path

        data_frame.to_csv(file_path, index=False)
    save_centroids_txt(centroids, file_path)
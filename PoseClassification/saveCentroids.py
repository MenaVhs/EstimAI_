import os

def save_centroids_txt(centroids, path):
    # Crear una carpeta por defecto llamada "Centroids" si no existe en la ruta especificada
    folder_name = os.path.join(os.path.dirname(path), 'Centroids')
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Crear un nombre de archivo único para los centroides
    filename = os.path.join(folder_name, 'centroids.txt')
    file_exists = os.path.exists(filename)
    n = 1
    while file_exists:
        filename = os.path.join(folder_name, f'centroids ({n}).txt')
        file_exists = os.path.exists(filename)
        n += 1

    # Guardar los centroides en un archivo de texto en la carpeta "Centroids"
    with open(filename, 'w') as f:
        for centroid in centroids:
            f.write(f'{centroid}\n')
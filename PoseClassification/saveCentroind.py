import os


def save_centroids_txt(centroids):
    # Crear un nombre de archivo único para los centroides
    filename = 'centroides.txt'
    file_exists = os.path.exists(filename)
    n = 1
    while file_exists:
        filename = f'centroids ({n}).txt'
        file_exists = os.path.exists(filename)
        n += 1

    # Guardar los centroides en un archivo de texto
    with open(filename, 'w') as f:
        for centroid in centroids:
            f.write(f'{centroid}\n')
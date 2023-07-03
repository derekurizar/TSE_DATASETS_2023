import shutil
import sys

# Read variables from command line
mesa = sys.argv[1]

import os

def find_files_with_string(directory, search_string):
    matching_file_names = []
    
    for file_name in os.listdir(directory):
        if search_string in file_name:
            matching_file_names.append(file_name)
    
    return matching_file_names


files = find_files_with_string("./actas_malas", "mesa_"+mesa)

if len(files) == 0:
    print("No se encontraron archivos")
else:
  for file in files:
    shutil.move("./actas_malas/"+file, "./actas_procesadas/"+file)


# Ruta y nombre del archivo a mover
#archivo_a_mover = './actas_malas/' + 'departamento_' + departamento + '_municipio_' + municipio + '_centro_' + centro + '_mesa_' + mesa + '.jpg'

# Ruta de la carpeta de destino
#carpeta_destino = './actas_procesadas/'

# Mover el archivo a la carpeta de destino
#shutil.move(archivo_a_mover, carpeta_destino)

# Ruta y nombre del archivo a mover
#archivo_a_mover = './actas_malas/'+ 'departamento_' + departamento + '_municipio_' + municipio + '_centro_' + centro + '_mesa_' + mesa + '.json'

# Ruta de la carpeta de destino
#carpeta_destino = './actas_procesadas/'

# Mover el archivo a la carpeta de destino
#shutil.move(archivo_a_mover, carpeta_destino)
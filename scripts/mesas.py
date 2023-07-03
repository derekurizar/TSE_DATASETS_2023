import os
import csv


def get_json_files_in_directory(directory):
    json_files = []
    for file in os.listdir(directory):
        if file.endswith(".json"):
            json_files.append(file)
    return json_files


def parse_filename(filename):
    parts = filename.split('_')
    departamento = parts[1]
    municipio = parts[3]
    centro = parts[5]
    mesa = parts[7].split('.')[0]
    return departamento, municipio, centro, mesa


def build_hierarchy(json_files):
    departamentos = {}
    for file in json_files:
        departamento, municipio, centro, mesa = parse_filename(file)
        if departamento not in departamentos:
            departamentos[departamento] = {}
        if municipio not in departamentos[departamento]:
            departamentos[departamento][municipio] = {}
        if centro not in departamentos[departamento][municipio]:
            departamentos[departamento][municipio][centro] = []
        departamentos[departamento][municipio][centro].append(mesa)
    return departamentos


def create_mesas_csv(hierarchy, file):
    with open(file, 'w', newline='') as csvfile:
        fieldnames = ['Departamento', 'Municipio', 'Centro', 'Mesa']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for departamento, municipios in hierarchy.items():
            for municipio, centros in municipios.items():
                for centro, mesas in centros.items():
                    for mesa in mesas:
                        writer.writerow(
                            {'Departamento': departamento, 'Municipio': municipio, 'Centro': centro, 'Mesa': mesa})


# Example usage
directory_path = "./datasets/0/actas_malas"
json_files = get_json_files_in_directory(directory_path)
hierarchy = build_hierarchy(json_files)
create_mesas_csv(hierarchy, './datasets/0/mesas.csv')

import pandas as pd
import json

spreadsheet_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQzGTA_NLqFVD_2z9mO7KxPTpnWDQz3Prnxc1j0TONwM6gbZoQTmaHtjSOp1RIjjBCQ6riSTiJjqrZX/pub?output=csv'
df = pd.read_csv(spreadsheet_url, sep=',')

# Filtra los datos para obtener aquellos con "Correcta" en "Verificación 1 (verificador)"
filtered_data_correctos = df[df['Verificación 1\n(verificador)'] == "Correcta"]
filtered_data_incorrectos = df[df['Verificación 1\n(verificador)'] == "Incorrecta"]

# Extrae solo los números de mesa
numeros_mesa_correctos = filtered_data_correctos['Mesa'].tolist()
numeros_mesa_incorrectos = filtered_data_incorrectos['Mesa'].tolist()

total_mesas_correctas = len(numeros_mesa_correctos)
total_mesas_incorrectos = len(numeros_mesa_incorrectos)
mesas_contadas = total_mesas_correctas + total_mesas_incorrectos

data = {
    'mesas_contadas': mesas_contadas,
    'total_mesas_correctas': total_mesas_correctas,
    'total_mesas_incorrectos': total_mesas_incorrectos,
    'numeros_de_mesa_correctos': numeros_mesa_correctos,
    'numeros_de_mesa_incorrectos': numeros_mesa_incorrectos,
}

# Exporta el diccionario como archivo JSON
with open('numeros_mesa.json', 'w') as file:
    json.dump(data, file)

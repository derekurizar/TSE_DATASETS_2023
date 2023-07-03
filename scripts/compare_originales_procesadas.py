import os
import json

from collections import defaultdict

def accumulate_votes(directory):
    # Get the list of files in the directory
    file_list = os.listdir(directory)

    # Accumulate total votes per departamento and party
    total_votes = defaultdict(lambda: defaultdict(int))

    # Process each JSON file
    for file in file_list:
        if file.endswith('.json'):
            file_path = os.path.join(directory, file)
            
            with open(file_path) as f:
                data = json.load(f)
                
                # Extract departamento number from the filename
                departamento_number = int(file.split('_')[1])
                
                # Process each record in the file
                for record in data:
                    partido = record["partido"]
                    votos = int(record["votos"])
                    
                    # Accumulate the votes for each party and departamento
                    total_votes[departamento_number][partido] += votos
    
    return total_votes

def compare_votes(directory1, directory2):
    # Accumulate votes for the first directory
    votes1 = accumulate_votes(directory1)
    
    # Accumulate votes for the second directory
    votes2 = accumulate_votes(directory2)
    
    # Compare the votes and calculate the percentage variation
    variation = defaultdict(dict)
    for departamento, parties1 in votes1.items():
        parties2 = votes2[departamento]
        for partido, votos1 in parties1.items():
            votos2 = parties2.get(partido, 0)
            if votos1 == 0:
                percent_variation = "N/A"
            else:
                percent_variation = (votos2 - votos1) / votos1 * 100
            variation[departamento][partido] = {
                'votos1': votos1,
                'votos2': votos2,
                'variation': percent_variation
            }
    
    return variation, votes1, votes2

# Example usage
directory1 = os.path.join(os.getcwd(), 'datasets/0/actas_originales')
directory2 = os.path.join(os.getcwd(), 'datasets/0/actas_procesadas')
result, votes1, votes2 = compare_votes(directory1, directory2)

# Print the percentage variation
for departamento, parties_variation in result.items():
    print(f"Departamento {departamento}:")
    for partido, data in parties_variation.items():
        votos1 = data['votos1']
        votos2 = data['votos2']
        percent_variation = data['variation']
        if percent_variation == "N/A":
            print(f"  {partido}: {votos1} originales vs {votos2} procesadas. Variación: {percent_variation}")
        else:
            print(f"  {partido}: {votos1} originales vs {votos2} procesadas. Variación: {percent_variation:.2f}%")

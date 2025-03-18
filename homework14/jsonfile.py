import os
import json

os.system('cls')

clubs = {
    'Antipods': {'country': 'Australia', 'wins': 10},
    'WeUnited': {'country': 'Estonia', 'wins': 16},
    'Kapibaras': {'country': 'Brazil', 'wins': 7},
    'Tango': {'country': 'Argentina', 'wins': 19},
    'JustChill': {'country': 'Jamaica', 'wins': 5},
}

with open('teams.json', 'w') as file:
    json.dump(clubs, file)

with open('teams.json') as file:
    data = json.load(file)

winner = max(data, key=lambda x: data[x]["wins"])
print(f'{winner}: {data[winner]}')

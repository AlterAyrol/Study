import json
import requests


# bb_req = requests.get('https://breakingbadapi.com/api/deaths')
# test1 = json.loads(bb_req.text)
# with open('my_test.json', 'w') as file:
#     json.dump(test1, file, indent=4)


bb2_req = requests.get(' https://www.breakingbadapi.com/api/deaths')
data = json.loads(bb2_req.text)
max_death = 0
for elem in data:
    if elem['number_of_deaths'] > max_death:
        max_death = elem['number_of_deaths']
for elem in data:
    if elem['number_of_deaths'] == max_death:
        with open('max_death.json', 'w') as file:
            json.dump(elem, file)
with open('max_death.json', 'r') as file:
    data = json.load(file)
for i in data:
    print(i, ':', data[i])

#5. Список погибших. - на сайте нет списка из 167 пассажиров погибших в этом эпизоде
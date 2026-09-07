import requests

r = requests.get('http://api.open-notify.org/astros.json')

print("find out how many people are in space at the moment:")

json = r.json()


print("there are a total of:", json.get('number'), "people in space.")

for peeps in json['people']:
    print(peeps['name'], "is on the", peeps['craft'])


    


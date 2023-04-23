import requests

print("WELCOME TO THE COUNTRY EXPLORER!")
country = input("Enter a country name: ")

url = f"https://restcountries.com/v2/name/{country}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()[0]
    print(f"NAME: {data['name']}")
    print(f"CAPITAL: {data['capital']}")
    print(f"POPULATIONS: {data['population']}")
    print(f"CURRENCY: {data['currencies'][0]['name']} ({data['currencies'][0]['symbol']})")
else:
    print("Sorry, could not fetch data for that country.")

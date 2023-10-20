import requests

# making api calls
response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)

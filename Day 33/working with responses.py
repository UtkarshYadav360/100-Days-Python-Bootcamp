import requests

# working with responses
response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.status_code)  # gets the status/response code from the API


# getting data from an APi
data = response.json()
print(data)

iss_position = response.json()["iss_position"]
print(iss_position)

longitude = response.json()["iss_position"]["longitude"]
print(longitude)

latitude = response.json()["iss_position"]["latitude"]
print(latitude)


# raising an exception
response.raise_for_status()

import requests

# parameters
parameters = {
    "amount": 10,
    "type": "boolean",
}

# getting response from the API
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

# getting the response/data in json format
data = response.json()
question_data = data["results"]

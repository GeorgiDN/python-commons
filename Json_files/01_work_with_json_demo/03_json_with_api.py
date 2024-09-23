import json
from urllib.request import urlopen
from urllib.error import HTTPError

# Free public API for exchange rates
url = "https://api.exchangerate-api.com/v4/latest/USD"

try:
    with urlopen(url) as response:
        source = response.read()

    data = json.loads(source)  # converts the raw JSON (received as bytes or a string) into a Python dictionary
    # print(json.dumps(data, indent=4))  # dictionary as a JSON-formatted string
    for currency, rate in data["rates"].items():
        print(currency, rate)


except HTTPError as e:
    print(f"HTTPError: {e.code} - {e.reason}")

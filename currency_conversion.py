import requests
import json


# function returning a maximum credit amount and currency value
def get_conversion(base, amount, convert='EUR'):
    url = 'https://api.exchangeratesapi.io/latest?base='

    r = requests.get(url + base)

    data = json.loads(json.dumps(r.json()))

    max_credit = (round(float(amount) * data['rates'][convert], 2))
    max_credit_currency = convert

    return max_credit, max_credit_currency

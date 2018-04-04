# First attempt to make a REST API call for LUIS

import requests

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '',
}

params ={
    # Query parameter
    'q': 'I want to order a pizza',
    # Optional request parameters, set to default values
    'timezoneOffset': '0',
    'verbose': 'false',
    'spellCheck': 'false',
    'staging': 'false',
}

try:
    r = requests.get('',headers=headers, params=params)
    print(r.json())

except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

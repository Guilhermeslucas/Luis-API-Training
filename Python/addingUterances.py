# Really simple code that helps me to create a entity with luis programatically

import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '',
}

data = open('utterances.json', encoding='UTF8')
data = data.read()

try:
    conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/luis/api/v2.0/apps/a4d2dae2-f847-4f86-8b17-147b90da0040/versions/0.1/examples", data.encode('UTF8'), headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))




import requests
import json
def sendtextmessage(message,contact):
    url = "https://www.fast2sms.com/dev/bulk"

    querystring = {"authorization": "tn4bwR3UViaoCfxJh9SY2qM8Ng0ZsGp56QzFkXcu7reBdPDvAONmu3D4zIwHcYREP8Wd0TixlSqAp6Gn", "sender_id": "FSTSMS", "message": message,
                   "language": "english", "route": "p", "numbers": "contact"}

    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)


    json_data=response.text
    d1=json.loads(json_data)
    return d1['return']
from config import webhook
from sign import getDingSign
import urllib3
import json
import requests
def sendmsg(title,msg):
    headers = {
        'Content-Type': 'application/json',
    }
    params = getDingSign()
    params['access_token'] = webhook
    message = {
        "msgtype": "markdown",
        "markdown": {
            "title": title,
            "text": msg
        },
        "at":{
            "atMobiles": [
                ""
            ],
            "atUserIds": [
                ""
            ],
            "isAtAll": False
        }
    }
    data = json.dumps(message)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    response = requests.post('https://oapi.dingtalk.com/robot/send', headers=headers, params=params, data=data,verify=False)
    print(response.json())
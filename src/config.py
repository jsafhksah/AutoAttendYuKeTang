import os

USER_INFO = os.getenv('USER_INFO')
PUSH_KEY = os.getenv('PUSH_KEY')
secret = os.getenv('SECRET')
webhook = os.getenv('WEBHOOK')

USER_INFO_ARR = USER_INFO.split("|", 1)
USERNAME = USER_INFO_ARR[0]
PASSWORD = USER_INFO_ARR[1]

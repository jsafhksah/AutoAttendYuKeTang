from urllib import request, parse
from datetime import datetime
from send import sendmsg
import time
from login import Login
from config import USERNAME, PASSWORD, PUSH_KEY
from urllib.parse import quote
import string

times = 900

def timer(n, task):
    count = 0
    while True: 
        count += 1
        if (count > times):
            msg = 'NotFoundOnlineClass'
            sendmsg(title='签到信息',msg=msg)
            print(msg)
            break

        result = task.enterOnlineClass()
        if (result[0]):
            msg = 'AttendSuccess'
            data = f"{msg}\n\n{result[1]}"
            sendmsg(title='签到成功',msg=data)
            print(msg + ' CourseName: ' + result[1])
            break
        print('The ' + str(count) + ' times did not success')
        time.sleep(n)


task = Login(username=USERNAME, password=PASSWORD)

print('init browser')
task.setBrowser()
task.login()
print('finish init browser')

timer(60, task)

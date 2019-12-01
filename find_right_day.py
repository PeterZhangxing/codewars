#/usr/bin/python3.5

import time,re

while True:

    input_date = input("input the date (example:2012-1-1): ")

    if input_date == "exit" or input_date == "quit":
        exit('exited from this programme!')

    exp = r'^(?:[1-9]{1}\d{3})-(?:[0]{,1}[0-9]{1}|[1]{1}[0-2]{1})-(?:[0]{,1}[0-9]{1}|[1-2]{1}[0-9]{1}|[3]{1}[01]{1})$'
    rexp = re.compile(exp)

    if rexp.match(input_date):
        try:
            print(time.strptime(input_date, "%Y-%m-%d").tm_yday)
        except Exception as e:
            print(e)
    else:
        print('invalid format of time')


# strftime() --> Takes one parameter, format, to specify the format of the returned string

import datetime

x = datetime.datetime.now()
m = x.strftime("%b")
print(x) # 2024-05-24 14:11:07.708579 
print(m) # 
print(datetime.datetime(2022,2,22))
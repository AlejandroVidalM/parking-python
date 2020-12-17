import random
from datetime import datetime

numero2=str(random.randrange(1000000)).zfill(6)
print(numero2)
var=f"hola {numero2}\nQue tal"
print(var)

old_date = datetime(2019, 2, 28, 10, 15, 00, 00000)
new_date = datetime(2019, 2, 28, 10, 25, 30, 00000)
print(new_date)
print(old_date)

minutes_diff = (new_date - old_date).total_seconds() / 60.0
print(minutes_diff)

from src.core.db import *


create_db()

resp = add_device("esp1", 25, 34)
print(resp)

data = get_data(1)
print(data)

resp_temp = update_temp(1, 27)
resp_humidity = update_humidity(1, 35)

print(resp_temp)
print(resp_humidity)

data = get_data(1)
print(data)
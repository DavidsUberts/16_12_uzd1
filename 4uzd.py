# using time
import time
import random

times=time.time()

password=f"{int(time.time()*1000)}-{random.randint(1000,9999)}"



print(password)
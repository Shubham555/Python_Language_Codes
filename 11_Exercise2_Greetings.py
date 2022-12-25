# time = int(input("Enter time in 24 hour clock: "))

# if(time>4 and time<=12):
#     print("Good Morning")

# elif(time>12 and time <=16):
#   print("Good Afternoon")

# elif(time>16 and time <=20):
#   print("Good Evening")

# elif(time>20 and time <=4):
#   print("Good Night")
from sqlite3 import Timestamp
import time
Timestamp = time.strftime('%H:%M:%S')
print(Timestamp)

Timestamp = int(time.strftime('%H'))
print(Timestamp)
Timestamp = int(time.strftime('%M'))
print(Timestamp)
Timestamp = int(time.strftime('%S'))
print(Timestamp)

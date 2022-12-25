# for i in range(12):
#   if(i == 10):
#     print("Skip the iteration")
#     continue
#   print("5 X", i, "=", 5 * i)
  
i = 0
while True:
  print(i)      # Prints/executes at least one time and then... checks the bottom condition
  i = i + 1
  if(i%1 == 0):  
    break
print("Exited the first loop\n")
i = 0
while True:
  print(i)      # Prints/executes at least one time and then... checks the bottom condition
  i = i + 1
  if(i%10 == 0):
    break
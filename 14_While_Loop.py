i = int(input("Enter the number: "))
print(i)
while(i<=38):
  i = int(input("Enter the number: "))
  print(i)

print("Done with the loop")

# i =0
# while(i<5):
#     print(i)
#     i=i+1
# print("Loop Exited")

i=5
while(i>0):
    print(i)
    i=i-1
else:
    print("I exited loop & i am Inside esle")    

# This isnormal syntax of do-while loop in C/C++,Java.

# do {
  # loop body;
# }while(condition);



# In-built do while loop is not there in python, therefore We emulated the do- while loop by urself using break statement

i = 0
while True:
  print(i)      # Prints/executes at least one time and then... checks the bottom condition
  i = i + 1
  if(i%1 == 0):  
    break
print("Exited the loops\n")    
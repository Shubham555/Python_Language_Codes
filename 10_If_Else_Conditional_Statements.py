a = int(input("Enter Your Age: "))
print("Your Age is: ",a)

#Conditional Operators
# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)

if(a>18):
    print("you can drive")
    print("yes")
else:
    print("You can not drive")
    print("No")
    print("Yay!")    


num = int(input("Enter The value of num: "))
if(num<0):
    print("Number is Negative")
elif(num==0):
    print("Number is Zero")
elif(num==999):
    print("Number is Special")    
else:
    print("Number is Positive")        

print("I am Happy")


num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")
    
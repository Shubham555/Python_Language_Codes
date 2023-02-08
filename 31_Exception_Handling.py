# a = input("Enter the number : ")
# print(f"Multiplication Table of {a} is: ")

# try:
#     for i in range(1,11):
#         print(f"{int(a)} X {i} = {int (a)*i}")
# except:
#     print("Invalid Input!")

# print("Some imp lines of Code")
# print("End of program")

try: 
    num = int(input("Enter an Integer: "))
    a = [6,3]
    print(a[num])
except ValueError:
    print("Number Entered is not an Integer. ")

except IndexError:
    print("Index Error")

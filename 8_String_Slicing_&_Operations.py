# Lec 12
names ="Harry,Shubham"
print(names[0:5])
print(len(names))

fruit = "Mango"
# Slicing
print(fruit[0:4]) #Including 0 but not 4
print(fruit[1:4]) #Including 1 but not 4
print(fruit[:])
print(fruit[:5])

# Negative Slicing
print(fruit[0:-3])   #In this len(fruit) added automatically like in below written
print(fruit[0:len(fruit)-3])

print(fruit[-1:len(fruit)-3]) #This will not print any thing
print(fruit[-3:-1]) #print(fruit[-3:len(fruit)-1])

#Loop Through a String

Word = "ABCDE"
for i in Word:
 print(i)

#Quick Quiz
name = "Harry"
print(name[-4:-2])

#Strings are Immutable
from turtle import heading


a = "!!!Harry !!!!!!!!! Harry "
print(len(a))
print(a.upper())  #String Obtianed by these are new string not original string is Changed
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Harry","john"))
print(a.split(" "))

blogheading = "introduction to js"
print(blogheading.capitalize())

str = "Welcome to the Course"
print(str.center(50))
print(len(str))
print(len(str.center(50)))
print(a.count("Harry"))

str1 = "Welcome to the Course !"
print(str1.endswith("!"))

str1 = "Welcome to the Course !"  #Varible is Overrided in Python
print(str1.endswith("to",4,10))


str2 = "Hii My Is Shubham Gite"
print(str2.find("Shu"))  # Retures Fisrt Occurence of that letter in String
print(str2.find("Shhh"))

print(str2.index("Sh"))
# print(str2.index("Shdfghg"))  # Gives Error

str3 = "WelcometotheCourse"
print(str3.isalnum())

str3 = "WelcometotheCourse"
print(str3.isalpha())

str4 = "welcometothecourse"
print(str4.islower())

str4 = "SHUBHAM"
print(str4.isupper())

str5 = "Hii My Is Shubham Gite\n"
print(str5.isprintable())

str6 = "     "
print(str6.isspace())

str7 = "Hii My Is Shubham Gite"
print(str7.istitle())
 

str8 = "Hii My Is Shubham Gite"
print(str8.startswith("Hii"))

str9 = "Hii My Is Shubham Gite"
print(str9.swapcase())

headings = "introduction to js"
print(headings.title())
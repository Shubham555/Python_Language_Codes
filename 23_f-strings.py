letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Harry"

print(letter.format(country,name))    # old method of formating using format keyword.
print(f"Hey my name is {name} and I am from {country}")   #new method of Formating using f-string.
print(f"We use f-strings like this : Hey my name is {{name}} and I am from {{country}}")
price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)
# print(txt.format())
print(f"{2 * 30}")
print(type(f"{2 * 30}"))
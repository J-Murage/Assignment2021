import datetime
name = input("Enter your name:")
age = int(input("Enter your age:"))
currentyear = datetime.datetime.now().year
dob = currentyear-age
print( dob+100)

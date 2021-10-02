userWeight =float(input("Please enter your weight:"))
userHeight =float(input("Please enter your Height:"))
userBmi =(userWeight * 703) / (userHeight ** 2)
if userBmi < 18.5:
    print("A person with a BMI of:" + str(userBmi) + "is underweight")
elif userBmi < 26:
    print("A person with a BMI of:" + str(userBmi) + \
          "has an optimal weight")
else:
    print("A person with a BMI of:" + str(userBmi) + \
          "is overweight")
weight = float(input("enter your weight: "))
height = float(input("enter your height: "))
bmi = weight / height**2
if bmi < 18.5:
    print("you are underweight")
elif bmi > 18.5 and bmi < 25:
    print("you have a normal weight")
elif bmi > 25 and bmi < 30:
    print("you are slightly overweight")
elif bmi > 30 and bmi < 35:
    print("you are obese")
elif bmi > 35:
    print ("you are clinically obese.")
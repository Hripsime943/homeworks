year = int(input("enter year number: "))
if year % 4 == 0 or year % 400 == 0:
    print ("Leap year")
else:
    print ("Not leap year")
    
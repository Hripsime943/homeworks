print ("Welcome to tashir pizza")
choice = input("please choose your pizzas size(small,medium & large): ")
small = 15
medium = 20
large = 25
total = 0
if choice == "small":
    total += small 
    peperonni = input("sorry, do you want peperoni?(Y or N) ")
    if peperonni == "Y": 
        total += 2
elif choice == "medium":
    total += medium
    peperonni = input("sorry, do you want peperoni?(Y or N) ")
    if peperonni == "Y": 
        total += 3
elif choice == "large":
    total += large
    peperonni = input("sorry, do you want peperoni?(Y or N) ")
    if peperonni == "Y": 
        total += 3
extra_cheese = input("do you want double cheese(Y or N): ")
if extra_cheese == "Y":
        total += 1
print (f"your bill will be {total}$")

names = ["Noro","Argisht","Levon", "es"]
ages = [23, 60, 30, 23]
for i in range(len(names)):
    print(f"{names[i]} is {ages[i]} years old.")
oldest_age = max(ages)
oldest_index = ages.index(oldest_age)
oldest_person = names[oldest_index]
print (f"The oldest person is {oldest_person}, age is {oldest_age}.")

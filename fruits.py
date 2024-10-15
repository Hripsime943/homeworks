fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    try:
        fruit = fruits[index]  
        print(fruit + " pie")
    except IndexError:
        print("Error: Index out of range. Please provide a valid index.")
make_pie(int(input("enter index number: ")))

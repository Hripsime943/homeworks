def fibonacci_recursive(num):
    if num <= 0:
        return "enter positive number:"
    elif num == 1:
        return 1
    else:
        return fibonacci_recursive(num - 1) + fibonacci_recursive(num - 2)
# num = int(input("Enter your value: "))
print (fibonacci_recursive(10))
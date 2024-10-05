total_sum = 0
while True:
    user_input = int(input("Enter a number (or 0 to stop): "))
    if user_input == 0:
        break  
    total_sum += user_input
    print(f"The sum of your numbers is: {total_sum}")
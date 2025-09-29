
while True:
    user_input = input("How many Fibonacci numbers do you want? ")
    if user_input.isdigit():
        number = int(user_input)
        if number > 0:
            break
        else:
            print("Please enter a number greater than 0.")
    else:
        print("Please enter a valid number.")

# Print Fibonacci sequence
a = 0
b = 1

for i in range(number): 
    print(a)
    next_number = a + b
    a = b
    b = next_number

import numbers 
user_input = input("Enter integer: ")
is_negative = False

if not user_input.lstrip("-").isdigit():
    print("Please input a number")

else:
    user_input = int(user_input)
    if user_input > 0 or user_input < 0:
        user_input *= -1
    print(user_input)



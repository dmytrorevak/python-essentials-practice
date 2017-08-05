print("What operation do you want to accomplish ?")
user_choice = input("+ - * / % \n")
if user_choice == "+":
    first_addition = float(input("Please enter the first addition "))
    second_addition = float(input("Please enter the second addition "))
    total_sum = str(first_addition + second_addition)
    print("Result is " + total_sum)
elif user_choice == "-":
    decreasing = float(input("Please enter the decreasing "))
    negative = float(input("Please enter the negative "))
    differance = str(decreasing - negative)
    print("Result is " + differance)
elif user_choice == "*":
    first_multiplier = float(input("Please enter the first multiplier "))
    second_multiplier = float(input("Please enter the second multiplier "))
    product = str(first_multiplier * second_multiplier)
    print("Result is " + product)
elif user_choice == "/":
    shared = float(input("Please enter the shared "))
    divider = float(input("Please enter the second divider "))
    fraction = str(shared / divider)
    print("Result is " + fraction)
elif user_choice == "%":
    shared = float(input("Please enter the shared "))
    divider = float(input("Please enter the second divider "))
    remainder = str(shared % divider)
    print("Result is " + remainder)
else:
    print("You entered incorrect symbol")

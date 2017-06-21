first_number = int(input("Please, enter the first number of the sequence: "))
second_number = int(input("Please, enter the second number of the sequence: "))
order_of_numbers = input("Enter '+' if you want growth numbers sequence or "
                         "enter '-' if you want decrease numbers sequence: ")

if order_of_numbers is "+":
    for i in range(first_number, second_number + 1):
        print(i)
elif order_of_numbers is "-":
    for i in reversed(range(first_number, second_number + 1)):
        print(i)
else:
    print("You have entered incorrect symbol")

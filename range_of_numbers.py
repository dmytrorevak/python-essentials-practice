first_number = int(input("Please, enter the first number of the sequence: "))
second_number = int(input("Please, enter the second number of the sequence: "))
order_of_numbers = input("Enter '+' if you want growth numbers sequence or "
                         "enter '-' if you want decrease numbers sequence: ")


if order_of_numbers is "+":
    # for i in range(first_number, second_number + 1):
    #     print(i)
    counter = first_number
    while counter <= second_number:
        print(counter)
        counter += 1
elif order_of_numbers is "-":
    # for i in reversed(range(first_number, second_number + 1)):
    #     print(i)
    counter = second_number
    while counter >= first_number:
        print(counter)
        counter -= 1
else:
    print("You have entered incorrect symbol")

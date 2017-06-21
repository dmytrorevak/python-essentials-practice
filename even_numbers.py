first_number = int(input("Please, enter the first number of the sequence: "))
second_number = int(input("Please, enter the second number of the sequence: "))


# for i in range(first_number, second_number + 1):
#     if not i % 2 and i != 0:
#         print(i)


counter = first_number
while counter <= second_number:
    if counter % 2 == 0 and counter != 0:
        print(counter)

    counter -= 1

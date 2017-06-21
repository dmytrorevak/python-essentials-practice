def integet_number_validation(entered_number):
    try:
        int(entered_number)
        return True
    except ValueError:
        return False


def count_sum_of_number(number):
    number_length = len(number)
    integer_number = int(number)
    result = 0

    for i in range(number_length):
        сurrent_bit_of_number = 10 ** (number_length - (i + 1))
        current_add = integer_number // сurrent_bit_of_number
        result += current_add
        integer_number -= current_add * сurrent_bit_of_number

    return result


entered_number = input("Please, enter some integer number: ")

is_entered_number_valid = integet_number_validation(entered_number)

if is_entered_number_valid:
    print(count_sum_of_number(entered_number))
else:
    print("You have entered not integer number!")

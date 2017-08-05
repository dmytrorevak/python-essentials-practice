from sum_of_number import count_sum_of_number

counter = 0

for i in range(1000):
    first_three_digit_sum = count_sum_of_number(i)

    for j in range(1000):
        second_three_digit_sum = count_sum_of_number(j)

        if first_three_digit_sum == second_three_digit_sum:
            counter += 1

print("There is: " + str(counter) + " lucky tickets")
print("Your chance to have it is: " + str(counter / 1000000 * 100) + " percentages")

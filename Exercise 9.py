previous_number = 0
for current_number in range(1, 11):
    sum_numbers = current_number + previous_number
    print(f"Current Number: {current_number}, Previous Number: {previous_number}, Sum: {sum_numbers}")
    previous_number = current_number

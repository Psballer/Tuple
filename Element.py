def sum_of_elements(numbers):
    outcome = []
    for inner_list in range (len(numbers[0])):
        sum_of_numbers = 0 
        for index in numbers:
            sum_of_numbers += index[inner_list]
            outcome.append(sum_of_numbers)
    return outcome
numbers = ([2, 3, 4], [1, 5, 7], [4, 6, 8])
print(sum_of_elements(numbers))

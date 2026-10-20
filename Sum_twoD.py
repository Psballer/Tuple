def add_number(numbers):
    outcome = []
    for inner_list in numbers:
        sum_of_numbers = sum(inner_list)
        outcome.append(sum_of_numbers)
    return outcome
numbers = ([2, 3, 4],[1, 5, 7,], [4, 6, 8])
print(add_number(numbers))
    
    

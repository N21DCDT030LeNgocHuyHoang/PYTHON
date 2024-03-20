def filter_dict_by_condition(dictionary, condition):
    filtered_dict = {}
    for key, value in dictionary.items():
        if condition(key, value):
            filtered_dict[key] = value
    return filtered_dict


my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Define a condition function to filter out even values
def is_even(key, value):
    return value % 2 == 0

filtered_dict = filter_dict_by_condition(my_dict, is_even)
print(filtered_dict)  # Output: {'b': 2, 'd': 4}

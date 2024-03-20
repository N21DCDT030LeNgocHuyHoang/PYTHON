def insert_value_at_beginning(original_tuple, value):
    # Convert the tuple to a list to allow insertion
    original_list = list(original_tuple)
    # Insert the value at the beginning of the list
    original_list.insert(0, value)
    # Convert the list back to a tuple
    new_tuple = tuple(original_list)
    return new_tuple

# Example usage:
original_tuple = (2, 3, 4)
value = 1
new_tuple = insert_value_at_beginning(original_tuple, value)
print(new_tuple)  # Output: (1, 2, 3, 4)

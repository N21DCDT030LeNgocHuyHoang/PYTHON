def get_key_with_highest_value(dictionary):
    if not dictionary:
        return None 

    max_key = max(dictionary, key=dictionary.get)
    return max_key
my_dict = {'a': 5, 'b': 9, 'c': 2}

result = get_key_with_highest_value(my_dict)
print("Key with the highest value:", result)

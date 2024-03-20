def merge_and_sum(dict1, dict2):
    merged_dict = dict1.copy()  
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
merged_dict = merge_and_sum(dict1, dict2)
print("Merged dictionary with sum of common keys:")
print(merged_dict)
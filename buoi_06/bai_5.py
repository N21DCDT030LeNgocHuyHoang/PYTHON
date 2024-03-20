def same_frequency(list1, list2):
    # Create dictionaries to count frequencies of elements in both lists
    freq_dict1 = {}
    freq_dict2 = {}

    for item in list1:
        freq_dict1[item] = freq_dict1.get(item, 0) + 1

    
    for item in list2:
        freq_dict2[item] = freq_dict2.get(item, 0) + 1
    
    return freq_dict1 == freq_dict2
list1 = [1, 2, 3, 4, 4, 5]
list2 = [5, 4, 4, 3, 2, 1]

print(same_frequency(list1, list2))  # Output: True

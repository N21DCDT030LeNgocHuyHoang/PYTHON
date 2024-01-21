def find_pairs_with_sum(arr, target_sum):
    pairs = set() 

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            current_sum = arr[i] + arr[j]

            if current_sum == target_sum:
                
                pairs.add((arr[i], arr[j]))

    return pairs

input_array = [2, 6, 3, 9, 11]
target_sum = 9

result_pairs = find_pairs_with_sum(input_array, target_sum)
print(result_pairs)

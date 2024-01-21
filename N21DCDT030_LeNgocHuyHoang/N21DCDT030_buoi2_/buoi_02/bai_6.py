def reverse(array):
    length = len(array)
    for i in range(length // 2):
        other = length - i - 1
        array[i], array[other] = array[other], array[i]

array = [1, 3, 6]
print("Original array:", array)
reverse(array)
print("Reversed array:", array)
def printUnorderedPairs(array):
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            print(array[i] ,",", array[j])

nhap_array = [3, 1, 0, 7]
printUnorderedPairs(nhap_array)
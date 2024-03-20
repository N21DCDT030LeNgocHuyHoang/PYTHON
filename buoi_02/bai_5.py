def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            for k in range(0,100000):
                print(str(arrayA[i]) + "," + str(arrayB[j]))
arrayA = [4, 2, 3]
arrayB = [4, 1,5]
printUnorderedPairs(arrayA, arrayB)
def foo(array):
    sum = 0
    product = 1
    for i in array:
        sum += i
    for i in array:
        product *= i
    print("Sum = " + str(sum) + ", Product = " + str(product))
arrayA = [9,10,11,2]
foo(arrayA)
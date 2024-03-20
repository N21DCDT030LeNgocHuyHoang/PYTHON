def extract_diagonal_elements(tuple_of_tuples):
    diagonal_elements = tuple_of_tuples[i,i+1] 
    for i in range(min(len(tuple_of_tuples), len(tuple_of_tuples[0]))):
        return diagonal_elements

tuple_of_tuples = ((1, 2, 3),
                   (4, 5, 6),
                   (7, 8, 9))

diagonal_elements = extract_diagonal_elements(tuple_of_tuples)
print(diagonal_elements)  

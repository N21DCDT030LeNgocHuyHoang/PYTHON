NewTuple=('a','b','c','d','e')
def searchTuple(p_tuple,element):
    for i in range(0,len(p_tuple)):
        if p_tuple[i]==element:
            return f"The{element} is found at {i} index"
    return 'The element is not found'
print(searchTuple(NewTuple,'b'))
    
    


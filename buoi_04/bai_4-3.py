a = input("string 1: ")
b = input("string 2: ")
def check(s1, s2):
    if(sorted(a)== sorted(b)):
        print("are anagrams.") 
    else:
        print("are not anagrams.")
check(a,b)
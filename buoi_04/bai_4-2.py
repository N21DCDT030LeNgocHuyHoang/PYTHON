def anagram(tu1,tu2):
    clean_tu1 =''.join(tu1.split()).lower()
    clean_tu2 =''.join(tu2.split()).lower()
    return sorted(clean_tu1) == sorted(clean_tu2)
tu1="restful"
tu2="fluster"
result = anagram(tu1,tu2)
if result:
    print(f"{tu1}and {tu2} are anagrams")
else:
    print(f"{tu1}and {tu2} are not anagrams")
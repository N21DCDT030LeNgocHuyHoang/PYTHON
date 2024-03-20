def is_anagram_recursive(s1, s2):
    if not s1:
        return not s2
    if s1[0] in s2:
        return is_anagram_recursive(s1[1:], s2.replace(s1[0], '', 1))
    else:
        return False
tu1 = "restful"
tu2 = "fluster"
result = is_anagram_recursive(tu1, tu2)
if result:
    print(f"{tu1} và {tu2} are anagrams")
else:
    print(f"{tu1} và {tu2} are not anagrams")

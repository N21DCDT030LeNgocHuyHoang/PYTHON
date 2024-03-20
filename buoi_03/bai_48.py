sentence = ' My name is E'
def is_consonant(letter):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return letter.isalpha() and letter.lower()not in vowels
consonant= [i for i in sentence if is_consonant(i)]
print(consonant)
def count_word_frequency(word_list):
    count = {}
    for word in word_list:
        count[word] = count.get(word, 0) + 1
    return count

def main():
    my_list = ["apple", "banana", "apple", "orange", "banana", "apple"]
    result = count_word_frequency(my_list)
    print("Số lần xuất hiện của từng từ:")
    print("Apple:", result.get("apple", 0))
    print("Banana:", result.get("banana", 0))
    print("Orange:", result.get("orange", 0))

if __name__ == "__main__":
    main()
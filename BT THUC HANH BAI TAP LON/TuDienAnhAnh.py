import pickle

class ListNode:
    def __init__(self, part_of_speech, meaning, example):
        self.part_of_speech, self.meaning, self.example = part_of_speech, meaning, example
        self.next = None

class BSTNode:
    def __init__(self, word):
        self.word, self.meanings, self.left, self.right = word, None, None, None

class Dictionary:
    def __init__(self):
        self.hash_table = {}

    def _hash(self, word):
        return word[0].lower()

    def _insert_bst(self, root, word):
        if not root: return BSTNode(word)
        setattr(root, 'left' if word < root.word else 'right', 
                self._insert_bst(getattr(root, 'left' if word < root.word else 'right'), word))
        return root

    def _find_bst(self, root, word):
        return root if not root or root.word == word else self._find_bst(getattr(root, 'left' if word < root.word else 'right'), word)

    def add_word(self, word, part_of_speech, meaning, example):
        key, node = self._hash(word), self.hash_table.setdefault(self._hash(word), BSTNode(word))
        setattr(self._find_bst(node, word), 'meanings', ListNode(part_of_speech, meaning, example) if not node.meanings else getattr(node.meanings, 'next', 
                                                                                                                                                setattr(node.meanings, 'next', ListNode(part_of_speech, meaning, example))))

    def remove_word(self, word):
        node = self._find_bst(self.hash_table.get(self._hash(word)), word)
        if not node: return False
        if not node.left: return node.right, True
        if not node.right: return node.left, True
        temp = self._find_min(node.right)
        node.word, node.meanings = temp.word, temp.meanings
        node.right = self._delete_bst(node.right, temp.word)[0]
        return node, True

    def _delete_bst(self, root, word):
        if not root: return root, False
        setattr(root, 'left' if word < root.word else 'right', self._delete_bst(getattr(root, 'left' if word < root.word else 'right'), word))
        return root, True

    def _find_min(self, root):
        return root if not root.left else self._find_min(root.left)

    def lookup(self, word):
        node = self._find_bst(self.hash_table.get(self._hash(word)), word)
        return None if not node else [(node.meanings.part_of_speech, node.meanings.meaning, node.meanings.example) 
                                    for node in self._traverse(node.meanings)]

    def _traverse(self, node):
        return [] if not node else [node] + self._traverse(node.next)

    def save_to_file(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.hash_table, f)

    def load_from_file(self, filename):
        with open(filename, 'rb') as f:
            self.hash_table = pickle.load(f)

def main():
    dictionary, filename = Dictionary(), 'your_student_id_bam'
    menu = {'1': lambda: dictionary.add_word(input("Nhập từ: "), input("Nhập loại từ: "), input("Nhập nghĩa: "), input("Nhập ví dụ: ")),
            '2': lambda: print("Đã loại bỏ mục từ.") if dictionary.remove_word(input("Nhập từ cần loại bỏ: ")) else print("Không tìm thấy mục từ."),
            '3': lambda: [print(f"Nghĩa {idx+1}:\n  Loại từ: {pos}\n  Nghĩa: {meaning}\n  Ví dụ: {example}") 
for idx, (pos, meaning, example) in enumerate(dictionary.lookup(input("Nhập từ cần tra cứu: ")) or ["Không tìm thấy mục từ."])],
            '4': lambda: [dictionary.save_to_file(filename), print("Đã lưu từ điển vào tập tin.")],
            '5': lambda: [dictionary.load_from_file(filename), print("Đã nạp từ điển từ tập tin.")],
            '6': lambda: exit()}
    while True:
        print("1. Thêm một mục từ mới vào từ điển\n2. Loại bỏ một mục từ của từ điển\n3. Tra cứu các nghĩa của một m

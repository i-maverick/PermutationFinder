class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = dict()
        self.last = False


class PrefixTree:
    PREFIX_FOUND = 0
    WORD_FOUND = 1

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for letter in word:
            if letter not in node.next:
                node.next[letter] = Node(letter)
            node = node.next[letter]
        node.last = True

    def find(self, _word):
        node = self.root
        for letter in _word:
            if letter not in node.next:
                return None
            node = node.next[letter]
        return self.WORD_FOUND if node.last else self.PREFIX_FOUND


def load_from_file(tree, filename):
    with open(filename, encoding='utf-8') as file:
        for line in file:
            word = line.strip()
            if word:
                tree.insert(word)

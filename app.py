# -*- coding: utf-8 -*-

from itertools import permutations
from typing import Set

from prefix_tree import PrefixTree, load_from_file


MIN_WORD_LENGTH = 6  # minimal word length to be counted
MIN_PERMUTATIONS = 5  # minimal number of permutations
PREFIX_LENGTH = 4  # length of prefix to filter words


def create_prefix_set(prefix_tree: PrefixTree, word: str) -> Set:
    prefix_set = set()
    for prefix in (''.join(item) for item in permutations(word, PREFIX_LENGTH)):
        if prefix_tree.find(prefix) is not None:
            prefix_set.add(prefix)
    return prefix_set


def find_permutations(prefix_tree: PrefixTree, word: str) -> None:
    """
    Find permutations for word from loaded prefix tree
    :param prefix_tree: loaded prefix tree with known words
    :param word: source word for permutations
    """
    prefix_set = create_prefix_set(prefix_tree, word)
    found_words = set()
    for i in range(MIN_WORD_LENGTH, len(word) + 1):
        for perm in (''.join(item) for item in permutations(word, i)):
            prefix = perm[0:PREFIX_LENGTH]
            if prefix not in prefix_set:
                continue

            if perm == word:
                continue

            result = prefix_tree.find(perm)

            if result == prefix_tree.WORD_FOUND and perm not in found_words:
                found_words.add(perm)

            if len(found_words) >= MIN_PERMUTATIONS:
                output = ' '.join(found_words)
                print(f'{word}: {output}')
                return


def main(filename: str) -> None:
    """Main function for finding permutations from vocabulary"""
    tree = PrefixTree()
    load_from_file(tree, filename)

    with open(filename, encoding='utf-8') as file:
        for line in file:
            word = line.strip()
            if word:
                find_permutations(tree, word)


if __name__ == '__main__':
    main('russian_nouns.txt')

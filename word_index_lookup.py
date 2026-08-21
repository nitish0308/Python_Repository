from collections import defaultdict
from typing import List

def find_word_indices(group_a: List[str], group_b: List[str]) -> List[List[int]]:
    """
    For each word in group_b, return the 1-based indices where it appears in group_a.
    If a word does not appear, return [-1] for that word.

    :param group_a: List of words in group A
    :param group_b: List of words in group B
    :return: List of lists containing indices or [-1]
    """
    index_map = defaultdict(list)

    # Build index map for group A
    for i, word in enumerate(group_a, start=1):
        index_map[word].append(i)

    # Query for group B
    result = []
    for word in group_b:
        if word in index_map:
            result.append(index_map[word])
        else:
            result.append([-1])

    return result


def print_results(results: List[List[int]]) -> None:
    """
    Helper function to print results in the required format.
    """
    for res in results:
        print(*res)


if __name__ == "__main__":
    # Input handling (for competitive programming / CLI use)
    n, m = map(int, input().split())
    group_a = [input().strip() for _ in range(n)]
    group_b = [input().strip() for _ in range(m)]

    results = find_word_indices(group_a, group_b)
    print_results(results)
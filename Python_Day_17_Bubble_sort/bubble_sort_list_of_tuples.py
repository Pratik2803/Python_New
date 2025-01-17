from typing import List, Tuple


def sort_tuples_by_second_element_desc(tuples: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    """ Sorts a list of tuples by the second element (score) in descending order. """

    n = len(tuples)

    for i in range(n):
        # Track whether a swap was made
        swapped = False
        for j in range(0, n-i-1):
            if tuples[j][1] < tuples[j+1][1]:
                tuples[j], tuples[j+1] = tuples[j+1], tuples[j]
                swapped = True

        # Exit early if no swaps occurred
        if not swapped:
            break

    return tuples


students_scores = [("Alice", 90), ("Bob", 75),
                   ("Charlie", 85), ("Diana", 95), ("Eve", 70)]

print(sort_tuples_by_second_element_desc(students_scores))

from collections import Counter
from typing import Tuple


def guess(query: str, answer: str) -> Tuple[int, int, int, int, int]:
    """Compute the outcome of guessing a word

    Args:
        query (str): the word guessed
        answer (str): The actual word

    Returns:
        0: not found
        1: found but in worng position
        2: found in correct position
    """

    # Verify input
    assert len(query) == len(answer)
    size = len(answer)
    query = query.upper()
    answer = answer.upper()
    assert query.isalpha()
    assert answer.isalpha()

    # init data structure
    result = [0] * size
    exact_pos = [False] * size
    present_ans = [False] * size

    # compare
    for i in range(size):
        if query[i] == answer[i] and not present_ans[i]:
            result[i] = 2
            exact_pos[i] = True
            present_ans[i] = True

    for idx, i in enumerate(query):
        if not exact_pos[idx]:
            for jdx, j in enumerate(answer):
                if not present_ans[jdx] and i == j:
                    result[idx] = 1
                    present_ans[jdx] = True
                    break

    return tuple(result)


def test_guess():
    assert guess("AAAAA", "BBBBB") == (0, 0, 0, 0, 0)
    assert guess("ABCDE", "ABCDE") == (2, 2, 2, 2, 2)
    assert guess("AEFAA", "BAACD") == (1, 0, 0, 1, 0)
    assert guess("AEFAA", "BAACA") == (1, 0, 0, 1, 2)
    assert guess("AEFAA", "BAFCD") == (1, 0, 2, 0, 0)

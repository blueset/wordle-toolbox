from typing import Dict, Any
from statistics import stdev
import numpy as np
import gmpy2


def count(number: int) -> int:
    """Count 1s in a binary number

    Args:
        number (int): binary number

    Returns:
        int: count
    """
    return gmpy2.popcount(number)


def std_dev(groups: Dict[Any, int], size: int) -> float:
    values = [count(i) for i in groups.values()] + ([0] * (size - len(groups)))
    return stdev(values)

def entropy(groups, size):
    values = np.array([count(i) for i in groups.values() if i])
    if values.sum() < 1:
        return 0
    # print(values)
    p = values / values.sum()
    return -np.sum(p * np.log2(p))

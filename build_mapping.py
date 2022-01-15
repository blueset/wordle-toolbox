from itertools import product
from guess import guess
from typing import Dict, Set, Tuple, List
from multiprocessing import Pool
import pickle
from tqdm import tqdm
import sys


def calculate(i):
    idx, query, dict_ans = i
    outcomes: Dict[Tuple[int, int, int, int, int], Set[str]] = {}
    for iidx, word in enumerate(dict_ans):
        outcome: Tuple[int, int, int, int, int] = guess(query, word)
        if outcome not in outcomes:
            outcomes[outcome] = 0
        outcomes[outcome] |= 1 << iidx
    # mapping[query] = outcomes

    # print(query, *[len(j) for j in outcomes.values()])
    return (idx, outcomes)


if __name__ == "__main__":
    dict_ans: List[str] = [i.strip() for i in open(f"dict_ans")]
    dict_query: List[str] = [i.strip() for i in open(f"dict_query")]
    words = dict_ans + dict_query

    mapping = {}
    args = [(idx, i, dict_ans) for idx, i in enumerate(words)]

    with Pool(8) as pool:
        m = pool.imap_unordered(calculate, args)

        for k, v in tqdm(m, total=len(words)):
            mapping[k] = v

    with open("mapping", "wb") as f:
        pickle.dump(mapping, f)

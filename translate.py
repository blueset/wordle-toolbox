import pickle
from typing import List
import gmpy2
import json
import sys


if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(f"""
Translate a tree from pickle format to JSON.

Usage:
    {sys.argv[0]}
    {sys.argv[0]} stdev_tree
    {sys.argv[0]} entropy_tree
    """)
    exit()

tree_name = "entropy_tree"

if len(sys.argv) > 1:
    tree_name = sys.argv[1]

dict_ans: List[str] = [i.strip() for i in open(f"dict_ans")]
dict_query: List[str] = [i.strip() for i in open(f"dict_query")]
words = dict_ans + dict_query

def trans_guess(guess: int) -> str:
    return words[guess]


def trans_outcome(index: int) -> str:
    try:
        return dict_ans[index]
    except KeyError:
        print("id", index, "is not found")
        return None

def translate(node):
    if isinstance(node, tuple):
        guess = trans_guess(node[0])
        branches = {"".join(map(str, k)): translate(v) for k, v in node[1].items()}
        branches = {k: v for k, v in branches.items() if v is not None}
        return {
            "guess": guess,
            "outcomes": branches
        }
    elif node is None:
        return None
    else:
        return trans_outcome(node)


if __name__ == "__main__":
    base = pickle.load(open(f"{tree_name}", "rb"))
    result = translate(base)
    with open(f"{tree_name}.json", "w") as f:
        json.dump(result, f)


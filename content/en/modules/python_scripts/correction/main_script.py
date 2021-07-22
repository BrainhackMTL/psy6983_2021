#!/usr/bin/env python
import argparse
from useful_functions import change_case, get_words, join_words

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", type=str)
    parser.add_argument("--case", choices=["mixed", "lower", "upper"])
    args = parser.parse_args()

    if args.case == "lower":
        print(args.text.lower())
    elif args.case == "upper":
        print(args.text.upper())
    elif args.case == "mixed":
        words = get_words(args.text)
        words = [change_case(w) for w in words]
        print(join_words(words))

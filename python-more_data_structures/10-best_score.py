#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    best = next(iter(a_dictionary.values()))
    for key in a_dictionary:
        if a_dictionary[key] > best:
            who = key
    return who

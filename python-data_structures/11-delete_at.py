#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx > 0 or idx < len(my_list):
        for i in range(len(my_list)):
            if i == idx:
                del my_list[idx]
    return (my_list)

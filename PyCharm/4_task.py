#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_input():
    return input("Enter num: ")


def test_input(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


def str_to_int(num):
    return int(num)


def print_int(num):
    print(num)


if __name__ == "__main__":
    ent_num = get_input()
    if test_input(ent_num):
        str_to_int(ent_num)
        print_int(ent_num)
    else:
        print("Cant use 'str_to_int'")

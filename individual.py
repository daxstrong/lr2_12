#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def sort_list_decorator(func):
    def wrapper(string_input):
        numbers = func(string_input)
        sorted_numbers = sorted(numbers)
        return sorted_numbers

    return wrapper


@sort_list_decorator
def get_list(string_input):
    return list(map(int, string_input.split()))


if __name__ == "__main__":
    input_string = input("Введите строку из целых чисел, разделенных пробелами: ")
    sorted_result = get_list(input_string)
    print("Отсортированный список:", sorted_result)

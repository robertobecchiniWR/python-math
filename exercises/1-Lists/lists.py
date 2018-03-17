#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Exercise 1: Lists
#
# Complete the filter_positive_oneliner function to achieve the same
# functionality as filter_positive but only in one line, using list
# comprehension.

def filter_positive(numbers):
    positive_numbers = []

    for n in numbers:
        if n > 0:
            positive_numbers.append(n)
            
    return positive_numbers


def filter_positive_oneliner(numbers):
    return []



measurements = [-7.43, 11.09, -10.50, 6.62, -3.84, 9.98, -1.64, -7.16, 5.42, -31.48]

positive_measurements = filter_positive_oneliner(measurements)

print(positive_measurements)

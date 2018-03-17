#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def filter_positive(numbers):
    positive_numbers = []

    for n in numbers:
        if n > 0:
            positive_numbers.append(n)
            
    return positive_numbers


def filter_positive_2(numbers):
    return [] # <- a list created using list comprehension


###########################


measurements = [-7.43, 11.09, -10.50, 6.62, -3.84, 9.98, -1.64, -7.16, 5.42, -31.48]

positive_measurements = filter_positive(measurements)
#positive_measurements = filter_positive_2(measurements)

print(positive_measurements)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def filter_positive(numbers):
    return [x for x in numbers if x > 0]


###########################

# Read data from measurements.dat
# measurements = ...

positive_measurements = filter_positive(measurements)

# Write data to positive_measurements.dat
# ...

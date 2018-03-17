#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Exercise 3: FileIO
#
# Read the data from the file measurements.dat and write only the
# positive values to a file named positive_measurements.dat

def filter_positive(numbers):
    return [x for x in numbers if x > 0]


# Read data from measurements.dat
measurements = []

positive_measurements = filter_positive(measurements)

# Write data to positive_measurements.dat

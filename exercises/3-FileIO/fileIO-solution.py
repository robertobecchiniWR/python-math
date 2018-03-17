#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Exercise 3: FileIO - Solution
#
# Read the data from the file measurements.dat and write only the
# positive values to a file named positive_measurements.dat

def filter_positive(numbers):
    return [x for x in numbers if x > 0]


# Read data from measurements.dat
input_file = open("measurements.dat", "r")
measurements = [float(line) for line in input_file]
input_file.close()

positive_measurements = filter_positive(measurements)

# Write data to positive_measurements.dat
output_file = open("positive_measurements.dat", "w")
for x in positive_measurements:
    output_file.write(str(x) + "\n")

output_file.close()

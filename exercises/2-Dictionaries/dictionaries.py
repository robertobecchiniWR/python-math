#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Exercise 2: Dictionaries
#
# Complete the filter_nice function to return only the nice geometric
# figures, which are the following:
# - Green triangles
# - Circles with diameter <= 3
# - Yellow rectangles
# - Rectangles with area >= 7
    

def filter_nice(figures):
    nice_figures = []
    
    for figure in figures:
        pass # Your code here
            
    return nice_figures


figures = [
        {'name': 'triangle',
         'sides': [3, 4, 5],
         'color': 'blue'},
        {'name': 'circle',
         'radius': 1,
         'color': 'red'},
        {'name': 'square',
         'side': 2,
         'color': 'green'},
        {'name': 'rectangle',
         'sides': [3, 4],
         'color': 'yellow'}
        ]


nice_figures = filter_nice(figures)

print(nice_figures)

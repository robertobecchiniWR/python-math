#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Exercise 2: Dictionaries - Solution
#
# Complete the filter_nice function to return only the nice geometric
# figures, which are the following:
# - Green triangles
# - Circles with diameter <= 3
# - Yellow rectangles
# - Rectangles with area >= 7

def is_nice(figure):
    if figure['name'] == 'triangle' and figure['color'] == 'green':
        return True
    
    if figure['name'] == 'circle' and 2*figure['radius'] <= 3:
        return True
    
    if figure['name'] == 'square' and (figure['color'] == 'yellow' or figure['side']**2 >= 7):
        return True
    
    if figure['name'] == 'rectangle' and (figure['color'] == 'yellow' or figure['sides'][0]*figure['sides'][1] >= 7):
        return True
    
    return False
    

def filter_nice(figures):
    nice_figures = []
    
    for figure in figures:
        if is_nice(figure):
            nice_figures.append(figure)
            
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

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 11:37:20 2019

@author: aowang
"""
import random
import math

in_circle = 0
total = 0

# circle x^2 + y^2 = r^2
# square is 1 by 1
# circle radius = 1/2

record_accurate = 0;

while(True):
    # random x and y coordinates, - 0.5 <= x < 0.5, -0.5 <= y < 0.5
    rand_x = random.random() - 0.5
    rand_y = random.random() - 0.5
    
    # testing if random coordinates are on or inside the circle of radius 1/2
    r = math.sqrt(math.pow(rand_x,2)+math.pow(rand_y,2)) <= 1/2
    if(r):
        in_circle += 1
    total += 1
    
    # caluation of 4 * pi/4
    current_pi = 4 * in_circle/total
    
    function_pi = math.pi
    record_diff = math.fabs(record_accurate-function_pi)
    
    diff = math.fabs(current_pi-function_pi)
    
    #finding smallest difference of approximation and python's math library of pi
    if(diff < record_diff):
        record_accurate = current_pi
        print(record_accurate)
    

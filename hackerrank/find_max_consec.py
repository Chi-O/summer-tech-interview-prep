#!/bin/python3

import math
import os
import random
import re
import sys


def find_max(n):
    binary = str(bin(n)).replace("0b", "")
    curr_count = 1
    max_count = 0
    
    for i in range(len(binary)):
        if i < (len(binary) - 1) and binary[i] == binary[i + 1] == "1":
            curr_count += 1
        else:
            if curr_count > max_count:
                max_count = curr_count
            curr_count = 1
    
    return max_count


if __name__ == '__main__':
    n = int(125)
    
    print(find_max(n))
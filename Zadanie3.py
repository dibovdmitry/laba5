#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

import sys
if __name__ == '__main__':
    c = str(input("Впишите числа "))
    k = 0
    for i in range(len(c)):
        if c[i].isdigit():
            k = k + 1
        if c[i].isalpha():
            continue
        x = c[i]
    print("количество чисел:", k, ',max=', max(x))

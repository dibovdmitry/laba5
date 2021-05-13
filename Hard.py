#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

import sys
if __name__ == '__main__':
    p1 = input('Напишите первое предложение 1 ').split()
    p2 = input('Напишите второе предложение 2 ')
    print(*(i for i in p1 if i in p2))
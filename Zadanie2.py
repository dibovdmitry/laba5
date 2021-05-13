#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

import sys
if __name__ == '__main__':
    v = "undertaleq"
    v = v[len(v) - 1:len(v) // 2 - 1:-1] + v[len(v) // 2 - 1::-1]
    print(v)

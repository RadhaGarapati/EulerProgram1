# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 13:04:08 2020

@author: Krishh
"""


import datetime



def Sundays():
    ans = sum(1
                for y in range(1901, 2001)
                for m in range(1, 13)
                if datetime.date(y, m, 1).weekday() == 6)
    return str(ans)


if __name__ == "__main__":
    print(Sundays())
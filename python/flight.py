# -*- coding: utf-8 -*-
"""
@author:
@environment: Python 3.7
@file: flight.py
@time: 2019/9/13
"""
import re
from collections import Counter





if __name__ == "__main__":

    # Midnight: 0:00-6:00
    # Morning: 6:00-12:00
    # Afternoon: 12:00-18:00
    # Evening: 18:00-24:00
    flight = Counter()

    f = open('flight_out.txt', encoding='utf-8')
    while True:
        line = f.readline()
        if line == '':
            break
        if ':' in line:
            arrival = int(line.split(':')[1][-2:])

            print(arrival)
            if arrival < 5 or arrival == 23:
                flight['Midnight'] += 1
            elif arrival < 11:
                flight['Morning'] += 1
            elif arrival < 17:
                flight['Afternoon'] += 1
            else:
                flight['Evening'] += 1

    print(flight)



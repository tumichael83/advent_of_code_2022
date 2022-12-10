import os
import re

if __name__ == '__main__':
    with open(os.path.expanduser('~/Desktop/Advent of Code 2022/day4/input.txt'), 'r') as input:    
        contained = 0
        while (line := input.readline()[:-1]) != '':
            ranges = [int(i) for i in re.split('-|,', line)]
            contained += 1 if (ranges[2] - ranges[1]) * (ranges[0] - ranges[3]) >= 0 else 0

        print(contained)
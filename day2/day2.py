import os
#  rock      paper   scissors
#    A         B        C
#    1         2        3
#      X           Y          Z
# 0 for loss, 3 for draw, 6 for win

scores = {
    'A X\n' : 3 + 0,
    'B X\n' : 1 + 0,
    'C X\n' : 2 + 0,
    'A Y\n' : 1 + 3,
    'B Y\n' : 2 + 3,
    'C Y\n' : 3 + 3,
    'A Z\n' : 2 + 6,
    'B Z\n' : 3 + 6,
    'C Z\n' : 1 + 6,
}

if __name__ == '__main__':
    with open(os.path.expanduser('~/Desktop/Advent of Code 2022/day2/input.txt'), 'r') as cals:
        total = 0
        line = cals.readline()
        while line != '':
            total += scores[line]

            line = cals.readline()

    print(total)
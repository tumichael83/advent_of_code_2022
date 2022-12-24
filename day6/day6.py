import os

if __name__ == '__main__':
    with open(os.path.expanduser('~/Desktop/Advent of Code 2022/day6/input.txt'), 'r') as lines:
        input = lines.readline()

        for i in range(len(input) - 14):
            if len(set([c for c in input[i:i+14]])) == 14:
                print(i+14)
                break
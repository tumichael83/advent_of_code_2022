import os

if __name__ == '__main__':
    with open(os.path.expanduser('~/Desktop/Advent of Code 2022/day1/input.txt'), 'r') as cals:
        cals_1 = 0
        cals_2 = 0
        cals_3 = 0
        temp = 0
        line = cals.readline()
        while line != '':
            if line == '\n':
                if temp >= cals_1:
                    cals_3 = cals_2
                    cals_2 = cals_1
                    cals_1 = temp
                elif temp >= cals_2:
                    cals_3 = cals_2
                    cals_2 = temp
                elif temp > cals_3:
                    cals_3 = temp
                temp = 0
            else:
                temp += int(line[:-1])

            line = cals.readline()

    print(cals_1+cals_2+cals_3)

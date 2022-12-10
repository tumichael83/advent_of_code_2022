import os

if __name__ == '__main__':
    # with open(os.path.expanduser('~/Desktop/Advent of Code 2022/day3/input.txt'), 'r') as input:
    #     priorities = 0

    #     while (line := input.readline()[:-1]) != '':
    #         shared = set({})
    #         num_items = len(line)//2
    #         # the unique things in the first half
    #         for c in line[:num_items]:
    #             shared.add(c)

    #         # comparing to the second half
    #         for c in line[num_items:]:
    #             if c in shared:
    #                 shared.remove(c)
    #                 priorities += (ord(c) - 96) if c.islower() else (ord(c) - 64 + 26)

    #     print(priorities)

    with open(os.path.expanduser('~/Desktop/Advent of Code 2022/day3/input.txt'), 'r') as input:
        priorities = 0

        while (line1 := input.readline()[:-1]) != ''\
               and (line2 := input.readline()[:-1]) != ''\
               and (line3 := input.readline()[:-1]) != '':

            shared1 = set({})
            # the unique items in the first line
            for c in line1:
                shared1.add(c)

            shared2 = set({})
            for c in line2:
                if c in shared1:
                    shared2.add(c)

            for c in line3:
                if c in shared2:
                    priorities += (ord(c) - 96) if c.islower() else (ord(c) - 64 + 26)
                    break

        print(priorities)
import os

if __name__ == '__main__':
    with open(os.path.expanduser('~/Desktop/Advent of Code 2022/day5/input.txt'), 'r') as input:
        lines = input.readlines()

        boxes = [[lines[i][j:j+4].strip() for i in range(8) if lines[i][j:j+4] != 4*' '][::-1] for j in range(0, len(lines[0]), 4)]
        
        # num boxes; src; dest
        instructions = [[int(x) for x in line.split() if x.isnumeric()] for line in lines[10:]]

        print("initial")
        for stack in boxes:
            print(stack)

        for i in instructions:
            boxes[i[2]-1].extend(boxes[i[1]-1][-1*i[0]:])
            boxes[i[1]-1] = boxes[i[1]-1][:-1*i[0]]
        
        print("\nfinal")
        for stack in boxes:
            print(stack[-1])

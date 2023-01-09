import re
from collections import defaultdict

def get_all_files(directory):
    with open(directory) as f:        #reading input
        lines = f.readlines()
    return lines

def output(stacks):
    out=""
    for val in sorted(stacks.items()):
        out+=val[1][0]
    return out

def setup(input):
    instructions, crates= [], defaultdict(str)
    
    for lines in input:
        if lines[0] == "m":
            instructions.append(list(map(int,re.findall(r'\d+', lines))))
        else:
            for i, char in enumerate(lines):
                if char.isalpha():
                    crates[i//4 + 1] += char
    return instructions, crates

def move(stack, a, f, t ):   
    temp = stack[f][:a] 
    stack[f] = stack[f][a:]
    stack[t] = temp+stack[t]
    return stack

input = get_all_files("input.txt")

inst, stack = setup(input)

for a, f, t in inst:
    stack = move(stack, a, f, t)
print(output(stack))


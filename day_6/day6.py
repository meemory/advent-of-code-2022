from collections import Counter

def get_all_files(directory):
    with open(directory) as f:        #reading input
        lines = f.readlines()
    return lines

def setup(input):
    for i in range(len(input[0])):
        WC=Counter(input[0][(i):(i+14)])
        if len(WC) == 14:
            return i+14
    return "couldnt find"


input = get_all_files("input.txt")
print(setup(input))
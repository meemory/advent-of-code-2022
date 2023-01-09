def get_all_files(directory):
    with open(directory) as f:        #reading input
        lines = f.readlines()
    new_lst = [x[:-1] for x in lines]
    return new_lst

def solve(input):
    path="/home"
    dirs = {"/home":0}
    for line in input:
        if line.startswith("$ cd"):
            if line[5:] == "/":
                path = "/home"
            elif line[5:] == "..":
                path = path[:path.rfind("/")]
            else:
                path = path + "/" + line[5:]
                dirs.update({path:0})
        elif line[0].isdigit():
            size = int(line[:line.find(" ")])
            dir=path
            for i in range(path.count("/")):
                dirs[dir] += size
                dir = dir[:dir.rfind("/")]


    limit = 30000000 - (70000000 - dirs["/home"])
    valid = []

    output = 0

    for dir in dirs:
        if dirs[dir] < 100000:
            output += dirs[dir]
        if limit <= dirs[dir]:
            valid.append(dirs[dir])
    
    return min(valid)

print(solve(get_all_files("./input.txt")))
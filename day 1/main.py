with open('input.txt') as f:
    lines = f.readlines()
new_lst = [x[:-1] for x in lines]

cals = []
i=0
temp=0

for x in new_lst:
    if x != "":
        temp += int(x)
    else:
        i += 1
        cals.append(temp)
        temp=0

print(max(cals))
with open('input.txt') as f:
    lines = f.readlines()
new_lst = [x[:-1] for x in lines]

temp= ""
total= 0

priority = {}
p = 1
for key in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
	priority[key] = int(p)
	p += 1

i=0

for x in range(len(new_lst)//3):
    for y in new_lst[i]:
        if y in new_lst[i+1]: 
            if y in new_lst[i+2]: temp=y
        elif y in new_lst[i+2]: 
            if y in new_lst[i+1]: temp=y
    i+=3
    total = total + priority[temp]

print(total)
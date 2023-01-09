with open('input.txt') as f:
    lines = f.readlines()
new_lst = [x[:-1] for x in lines]
add1 = 0
add2 = 0

for x in new_lst:
    x=x.split(",")
    x1,x2 = x[0], x[1]
    x1, x2 = x1.split("-"), x2.split("-")
    l1, l2, r1, r2 = int(x1[0]), int(x1[1]), int(x2[0]), int(x2[1])

    val1,val2 =set(range(l1, l2+1)), set(range(r1, r2+1))


    if val1.issubset(val2) or val2.issubset(val1): 
        add1+=1

    if val1.intersection(val2): 
        add2+=1

print(add1, add2)

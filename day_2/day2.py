with open('input.txt') as f:
    lines = f.readlines()
new_lst = [x[:-1] for x in lines]

#A, X... Rock...1
#B, Y... Paper...2
#C, Z... Siccors...3
#lose...0
#draw...3
#win...6

points=0
temp=""

for x in new_lst:
    x.split(" ")
    if x[2] =="X":
        if x[0]=="A":
            points+=3
        elif x[0]=="B":
            points+=1
        elif x[0]=="C":
            points+=2
    elif x[2] =="Y":
        if x[0]=="A":
            points+=1+3
        elif x[0]=="B":
            points+=2+3
        elif x[0]=="C":
            points+=3+3
    elif x[2] =="Z":
        if x[0]=="A":
            points+=2+6
        elif x[0]=="B":
            points+=3+6
        elif x[0]=="C":
            points+=1+6
print(points)



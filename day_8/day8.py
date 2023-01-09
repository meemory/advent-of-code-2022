def get_all_files(directory):
    with open(directory) as f:        #reading input
        lines = f.readlines()
    new_lst = [x[:-1] for x in lines]
    return new_lst

def scenic(left, right, up, down, temp):
    score=1
    for lst in (left, right, up, down):
            tracker = 0
            for i in range(len(lst)):
                if lst[i] < temp:
                    tracker += 1
                elif lst[i] >= temp:
                    tracker += 1
                    break
            
            score *= tracker
    return score

def solve(input):
    ROWS= len(input)
    COLS= len(input[0])
    
    output= (ROWS *2) + (COLS-2)*2
    sc=[]

    for row in range(1,ROWS-1):
        for col in range(1,COLS-1):
            temp=input[row][col]

            left = [input[row][col-i] for i in range(1, col+1)]
            right = [input[row][col+i] for i in range(1, COLS-col)]
            up = [input[row-i][col] for i in range(1, row+1)]
            down = [input[row+i][col] for i in range(1, ROWS-row)]

            if temp>max(left) or temp>max(right) or temp>max(up) or temp>max(down):
                output+=1
            
            sc.append(scenic(left,right,up,down,temp))
            
            
    return output,max(sc)


lst=get_all_files("input.txt")

print(solve(lst))

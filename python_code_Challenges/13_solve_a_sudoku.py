total = set(range(1,10))

def check_hori(i, j):
    return total-set(grid[i])

def check_verti(i, j):
    verti = []
    for r in range(9):
        verti.append(grid[r][j])
    return total-set(verti)

def check_box(i, j):
    first=[0,1,2]
    second=[3,4,5]
    third=[6,7,8]
    find_box = [first, second, third]
    for l in find_box:
        if i in l:
            row = l
        if j in l:
            col = l
    
    box = []
    for x in row:
        for y in col:
            box.append(grid[x][y])
        return total-set(box)


def poss_values(i, j):
    values = check_box(i, j).intersection(check_verti(i,j)).intersection(check_hori(i,j))
    return values

def solve():
    for i in range(9):
        for j in range(9):
            if grid[i][j]==0:
                p_values = list(poss_values(i, j))
                if len(p_values)==1:
                    grid[i][j] = p_values[0]
                    


grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]


while(sum(sum(i) for i in grid)!=495):
    solve()

for row in grid:
    print(*row)

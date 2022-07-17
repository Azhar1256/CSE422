#Question_2

xCITY=open('Question2 input1.txt','r')
xCITY=xCITY.read()
xCITY=xCITY.splitlines()
x=int(xCITY.pop(0))
y=int(xCITY.pop(0))

base_arr=[(0,1),(-1,0),(1,0),(0,-1)]
grid=[]


minimumMinutes=0
numberOfHuman=0


for i in xCITY:
  j=i.split()
  grid.append(j)


explored=[[-1]*y for i in range(x)]



def bfs(i,j):
    global x,y
    explored[i][j]=0
    region = []
    region.append((i,j))

    while len(region)>0:
        w1 , w2=region.pop(0)

        for k in range(len(base_arr)):
            current_i, current_j = base_arr[k]
            current_i += w1
            current_j += w2

            if (current_i>=0 and current_i<x and current_j>=0 and current_j<y and explored[current_i][current_j] == -1 and grid[current_i][current_j] == 'H'):
                explored[current_i][current_j] = explored[w1][w2]+1
                region.append((current_i,current_j))


for i in range(x):
    for j in range(y):
        if(grid[i][j]=='A'):
            bfs(i,j)


for i in range(x):
    for j in range(y):
        if(explored[i][j]==-1 and grid[i][j]=='H'):
            numberOfHuman+=1
        if (explored[i][j] != -1 and grid[i][j] == 'H'):
            minimumMinutes = max(minimumMinutes,explored[i][j])

            

print('Time: '+str(minimumMinutes)+' minutes ')
if(numberOfHuman==0):
    print('No one survived ')
else:
    print(str(numberOfHuman)+' survived ')

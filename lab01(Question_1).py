#Question_1

InfectedTracker = open('Question1 input1.txt','r')
InfectedTracker = InfectedTracker.read()
InfectedTracker = InfectedTracker.splitlines()

base_arr=[(1,1),(1,0),(1,-1),(0,-1),(0,1),(-1,1),(-1,0),(-1,-1)]

region=[]
for i in InfectedTracker:
    region.append(i.split())


maximumRegion=0
dummyMaximumRegion=0


x=len(region)
y=len(region[0])
explored=[[0]*y for i in range(x)]



def dfs(i,j):
    explored[i][j]=1
    global dummyMaximumRegion,x,y
    dummyMaximumRegion = dummyMaximumRegion+1
    for k in range(len(base_arr)):
        current_i,current_j = base_arr[k]
        current_i += i
        current_j += j
        if(current_i>=0 and current_i<x and current_j>=0 and current_j<y and explored[current_i][current_j]==0 and region[current_i][current_j]=='Y'):
            dfs(current_i,current_j)

for i in range(len(region)):
    for j in range(len(region[i])):
      if(explored[i][j]==0 and region[i][j]=='Y'):
          dummyMaximumRegion=0
          dfs(i,j)
          maximumRegion=max(dummyMaximumRegion,maximumRegion)

print(maximumRegion)

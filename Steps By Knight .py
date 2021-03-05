def isSafe(temp,N,visited):
    if temp[0] <= N and temp[0] > 0 and temp[1] > 0 and temp[1] <= N and visited[temp[0]][temp[1]] == False:
        return True
    return False 


def stepKnighCAn(pos,N,visited,queue):
    rowSet = [2,2,1,-1,-2,-2,1,-1]
    colSet = [1,-1,-2,-2,-1,1,2,2]
    for i in range(len(rowSet)):
        temp = [pos[0],pos[1],pos[2]]
        temp[0] += rowSet[i]
        temp[1] += colSet[i]
        temp[2] += 1
        if isSafe(temp,N,visited):
            queue.append(temp)
 

def minimumStepsKnight(knightPos,targetPos,N):
    visited = [[False for _ in range(N+1)] for _ in range(N+1)]
    queue = []
    knightPos.append(0)
    queue.append(knightPos)
    ans = N*N
    while(queue):
        pos = queue.pop(0)
        if pos[0] == targetPos[0] and pos[1] == targetPos[1]:
            ans = min(ans,pos[2])             
        visited[pos[0]][pos[1]] = True
        stepKnighCAn(pos,N,visited,queue)
    return ans

def inorder(tree,n,index,v):
    if index >= n:
        return 
    inorder(tree,n,(2*index)+1,v)
    v.append(tree[index])
    inorder(tree,n,(2*index)+2,v)


def minimumSwaptomakeTreeBST(tree):
    v = []
    n = len(tree)
    inorder(tree,n,0,v)
    t = [[0,0] for _ in range(len(v))]
    for i in range(n):
        t[i][0],t[i][1] = v[i],i
    t.sort(key = lambda x : x[0])
    #Graph Minimum swap finding Techniique 
    vis = [False] *n
    ans = 0
    for i in range(n):
        if vis[i]:
            continue
        j = i
        cycle = 0
        while(vis[j] == False):
            vis[j] = True
            j = t[j][1]
            cycle += 1
        if cycle > 1:
            ans += cycle-1
    return ans


if __name__ == "__main__":
    tree = [5, 6, 7, 8, 9, 10, 11 ]
                   
    print(minimumSwaptomakeTreeBST(tree))
    

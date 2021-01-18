def check(arr1,arr2,n):
    Ad1 = [[] for _ in range(n[0]+1)]
    Ad2 = [[] for _ in range(n[0]+1)]

    for i in range(1,len(arr1),2):
        Ad1[arr1[i-1]].append(arr1[i])
        Ad2[arr2[i-1]].append(arr2[i])
    for i in range(1,n[0]):
        s = Ad1[i]
        q = Ad2[i]
        while (len(s) != 0 and len(q) != 0):
            if s[-1] != q[0]:
                return False
            s.pop()
            q.pop(0)
    return True

if __name__ == "__main__":
    for _ in range(int(input())):
        n = list(map(int,input().rstrip().split(" ")))
        arr1 = list(map(int,input().rstrip().split(" ")))
        arr2 = list(map(int,input().rstrip().split(" ")))
        if check(arr1,arr2,n) :
            print("1")
        else:
            print("0")

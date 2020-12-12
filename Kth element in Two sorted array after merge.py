def kthElement(arr1,arr2,N,M,K):
    i = 0
    j = 0
    main = 1
    while(i<N and j < M):
        if arr1[i] < arr2[j]:
            t = arr1[i]
            i += 1
        else:
            t = arr2[j]
            j += 1
        if main == K:
            return t
        main += 1

    while(i<N):
        if main == K:
            return arr1[i]
        i+= 1
        main += 1
    while(j<M):
        if main == K:
            return arr2[j]
        j += 1
        main += 1



if __name__ == "__main__":
    for _ in range(int(input())):
        N,M,K = map(int,input().rstrip().split(" "))
        arr1 = list(map(int,input().rstrip().split(" ")))
        arr2 = list(map(int,input().rstrip().split(" ")))
        print(kthElement(arr1,arr2,N,M,K))

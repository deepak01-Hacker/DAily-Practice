def majoityMoore(arr,n):
    maj = 0 
    count = 1
    for i in range(len(arr)):
        if arr[maj] == arr[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            maj = i
            count = 1

    return arr[maj]
        
def majorityElement(arr,n):
    ele_moore = majoityMoore(arr,n)
    count = arr.count(ele_moore)
    if count > n//2:
        return ele_moore
    else:
        return -1


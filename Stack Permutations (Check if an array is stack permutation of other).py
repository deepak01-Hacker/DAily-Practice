
def stackPermutation(arr1,arr2):
    stack = []
    i = 0
    j = 0
    while(i<len(arr1)):
        if stack == [] or stack[-1] != arr2[j]:
            stack.append(arr1[i])
            i += 1
        if stack[-1] == arr2[j]:
            stack.pop()
            j += 1
    if stack == []:
        return "Is possible"
    return "Not possible"


if __name__ == "__main__":
    arr1 = [1,2,3]
    arr2 = [2,1,3]
    print(stackPermutation(arr1,arr2))
    

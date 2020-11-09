def changeNumber(st,changer):
    n = len(st)
    result = 0
    i = 0
    if n == 1:
        return changer[st[0]]
    while(i < n):
        if i+1 < n and changer[st[i]] < changer[st[i+1]]:
            result += changer[st[i+1]] - changer[st[i]]
            i += 2
        else:
            result += changer[st[i]]
            i+=1
    return result
            
if __name__ == "__main__":
    for _ in range(int(input())):
        roman = input()
        map = {}
        map['I']=1
        map['V']=5
        map['X']=10
        map['L']=50
        map['C']=100
        map['D']=500
        map['M']=1000
        print(changeNumber(roman,map))

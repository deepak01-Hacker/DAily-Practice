def remove(st,n):
    if n == 0:
        return st
    elif st[n-1] == st[n]:
        st.pop(n)
    return remove(st,n-1)
        
    
if __name__ == "__main__":
    for _ in range(int(input())):
        st = list(input())
        print(''.join(remove(st,len(st)-1)))

def wordBreak(dic,st,n,result):
    for i in range(1,n+1):
        prefix = st[:i]

        if prefix in dic:

            if (i == n):
                result += prefix
                print(result)
                return
            wordBreak(dic,st[i:],n-i,result+prefix+" ")


if __name__ == "__main__":
    wordBreak(["i", "like", "sam", "sung", "samsung", "mobile", "ice", 
  "and", "cream", "icecream", "man", "go", "mango"],"ilikesamsungmobile",18,"")



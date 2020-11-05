def wordBreak(dictionary,word,length_word):
    if length_word == 0:
        return True
    container = set(st for st in dictionary)
    dp = [False] * (length_word+1)
    dp[0] = True
    
    for len in range(1,length_word+1):
        for start in range(0,len):
            if dp[start] and word[start:len] in container:
                dp[len] = True
                break
    return dp[length_word]

if __name__ == "__main__":
    for _ in range(int(input())):
        n_D = int(input())
        dictionary = list(input().split(" "))
        word = input()
        if wordBreak(dictionary,word,len(word)):
            print("1")
        else:
            print("0")

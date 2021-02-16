def findMaxLen(S):
  left = 0
  right = 0
  maxlen = 0
  for i in range(len(S)):
    if S[i] == "(":
      left += 1
    elif S[i] == ")":
      right += 1

    if left == right:
      maxlen = max(maxlen,2*right)
    elif right > left:
      right = 0
      left = 0
  left = 0
  right = 0
  for i in range(len(S)-1,-1,-1):
    if S[i] == "(":
      left += 1
    elif S[i] == ")":
      right += 1

    if left == right:
      maxlen = max(maxlen,2*right)
    elif right < left:
      right = 0
      left = 0
  return maxlen
  

if __name__ == "__main__":
  print(findMaxLen("((()))"))

def isBalanced(exp):
    stack = []
    for parenthesis in exp:
        if parenthesis == "]":
            if stack != [] and stack[-1] == "[":
                stack.pop()
            else:
                return False
        elif parenthesis == ")":
            if stack != [] and stack[-1] == "(":
                stack.pop()
            else:
                return False
        elif parenthesis == "}":
            if stack != [] and stack[-1] == "{":
                stack.pop()
            else:
                return False
        else:
            stack.append(parenthesis)
    if len(stack):
        return False
    return True
            

if __name__=="__main__":
    for _ in range(int(input())):
        exp = input()
        if isBalanced(exp):
            print("balanced")
        else:
            print("not balanced")
        
    

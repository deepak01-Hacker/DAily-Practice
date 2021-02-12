#User function Template for python3
'''
Function Arguments :
		@param  : s (given string containing parenthesis) 
		@return : boolean True or False
'''
def ispar(x):
    stack = []
    t = 0
    for brac in x:
        if brac == "}":
            if t == 0 or stack[-1] != "{":
                return False
            else:
                t -= 1
                stack.pop()
        elif brac == ")":
            if t == 0 or stack[-1] != "(":
                return False
            else:
                t -= 1
                stack.pop()
                
        elif brac == "]":
            if t == 0 or stack[-1] != "[":
                return False
            else:
                t -= 1
                stack.pop()
        else:
            stack.append(brac)
            t += 1
    return True if stack == [] else False
            

#User function Template for python3

'''
Function Arguments :
		@param  : S (given postfix expression)
		@return : return the desired value
'''
def isOperator(s):
    if op == '+' or op == '-':
        return True
    if op == '*' or op == '/':
        return True
    return 0
    
def applyOp(a, b, op):
     
    if op == '+': return a + b
    if op == '-': return b - a
    if op == '*': return a * b
    if op == '/': return b // a


def EvaluatePostfix(S):
    stack = []
    for i in range(len(S)):
        if S[i].isdigit():
            stack.append(int(S[i]))
        else:
            val1 = stack.pop()
            val2 = stack.pop()
            ans = applyOp(val1,val2,S[i])
            stack.append(ans)
    return str(stack[0])

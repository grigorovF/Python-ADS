def evaluateExpression(expression):
    stack = []

    for c in expression:
        if c == ')':
            B = (int)(stack.pop())
            operator = stack.pop()
            A = (int)(stack.pop())
            stack.pop()

            if operator == '+':
                stack.append(A+B)
            elif operator == '-':
                stack.append(A-B)
       
        else:
            stack.append(c)

    return (int(stack[0]))
        


expression = input()
result = evaluateExpression(expression)
print ("result = ", result)
from Stack import Stack
from library import library

newExp = []
stack = Stack()

# expresion = "4 * ( 5 + 6 - ( 8 / 2 ^ 3 ) - 7 ) - 1"
# expresion = "5 * ( 6 + 2 ) - 12 / 4"
# expresion = "3 * 4 / ( 3 + 1 )"
expresion = "( ( ( 1 / 2 ) + ( 1 / 2 ) + 1 ) / ( 1 / ( 2 + 5 - 4 - 1 ) ) ) ^ ( ( 1 / 2 ) + 1 ) - 5 + 5 / ( 2 - 1 )"

def isNumber(exp):
    try:
        float(exp)
        return True
    except ValueError:
        return False

def convertToPosfix(expresion):
    newExpresion = expresion.split(" ")
    for exp in newExpresion:
        if isNumber(exp):
            newExp.append(exp)
        else:
            if stack.isEmpty():
                stack.push(exp)
            else:

                if exp == ")":
                    for ope in reversed(stack.getValues()):
                        if ope == "(":
                            stack.pop()
                            break
                        else:
                            value = stack.pop()
                            newExp.append(value)
                else:
                    valueTop = stack.peek()
                    value1 = list(filter(lambda x: exp == x['value'], library))[0]
                    value2 = list(filter(lambda x: valueTop == x['value'], library))[0]

                    if value1['p_exp'] > value2['p_stack']:
                        stack.push(exp)
                    elif value1['p_exp'] <= value2['p_stack']:
                        value = stack.pop()
                        newExp.append(value)
                        stack.push(exp)

    while stack.size() > 0:
        for exp in reversed(stack.getValues()):
            if exp == "(":
                stack.pop()
            else:
                value = stack.pop()
                newExp.append(value)
    
    return " ".join(newExp)

def evaluateExpresion(expresion):
    newExpresion = expresion.split(" ")
    for exp in newExpresion:
        if isNumber(exp):
            stack.push(exp)
        else:
            value1 = float(stack.pop())
            value2 = float(stack.pop())

            if exp == "+":
                res = value2 + value1
                stack.push(res)
            elif exp == "-":
                res = value2 - value1
                stack.push(res)
            elif exp == "*":
                res = value2 * value1
                stack.push(res)
            elif exp == "/":
                res = value2 / value1            
                stack.push(res)
            elif exp == "^":
                res = value2 ** value1
                stack.push(res)
    
    response = stack.pop()
    return response

print("Posfijo: " + convertToPosfix(expresion))
print(f"Respuesta: {evaluateExpresion(convertToPosfix(expresion))}")

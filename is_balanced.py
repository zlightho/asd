from stack import Stack

def is_balanced(s: str) -> bool:
    stack = Stack() # создаем пустой стек

    # итерируемся по символам в строке s
    for char in s:
        if char == '(':
            stack.push('(')
        elif char == ')' and stack and stack.peek == '(':  
            stack.pop()  
        else:  
            return False

    return not stack
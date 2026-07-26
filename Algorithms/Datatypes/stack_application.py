from Stack import Stack

def check_brackets(statement):
    stack = Stack()

    for check in statement:
        if check in ('{', '[', '('):
            stack.push(check)

        elif check in ('}', ']', ')'):
            if stack.isEmpty():
                return False
            last = stack.pop()

            if last == '{' and check == '}':
                continue
            elif last == '[' and check == ']':
                continue
            elif last == '(' and check == ')':
                continue
            else:
                return False

    return stack.isEmpty()

test = (
    "{(foo)(bar)} [hello] (((this)is)a)test", 
    "{(foo)(bar)} [hello] (((this)is)atest"
    )

for i in test:
    result = check_brackets(i)
    print(f"Here is a String:[ {i} ] = {result}")

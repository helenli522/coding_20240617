from collections import deque

stack = deque()


def my_check(str):
    res = list()
    for i, char in enumerate(str):
        if char == '(':
            stack.append(i)
            res.append('x')
        elif char == ')':
            if len(stack) == 0:
                res.append('?')
            else:
                index = stack.pop()
                res[index] = ' '
                res.append(' ')
        else:
            res.append(' ')
        # print(res)
    return res


while True:
    try:
        line = input()
        ans = ''.join(my_check(line))
        print(ans)
    except EOFError:
        break

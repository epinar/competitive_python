

def appendElements(res, ch):
    if len(res) == 0 and ch != ")":
        return [ch]
    for i,s in enumerate(res):
        res[i] = s + ch
    return res

def getSolution(s, ch):
    sols = []
    for i in range(len(s)):
        if s[i] == ch:
            sols.append(s[:i]+s[i+1:])
    return sols

def findSolutions(res, ch):
    sols = []
    for i, s in enumerate(res):
        sols += getSolution(s, ch)
    sols = set(sols)
    return list(sols)

def findSolutionOpen(res, ch):
    sols = []
    for i, s in enumerate(res):
        sols += getSolution(s, ch)
    sols = set(sols)
    return list(sols)

def removeInvalidParentheses_not_working(s):

    ct = 0
    res = []

    for i in range(len(s)):
        ch = s[i]
        res = appendElements(res, ch)
        print(i, ch, ct, res)
        if ch == '(':
            ct += 1
        elif ch == ')':
            if ct > 0:
                ct -= 1
            else:
                print("call")
                res = findSolutions(res, ch)

    while ct > 0:
        res = findSolutionOpen(res, ch)
        ct -= 1

    return res


def removeInvalidParentheses(s):

    # Build up all possible strings at each step.
    # Once there is a ( or ), either use it in the string and increase
    # left or right, or do not use it and decrease left_rem or right_rem.
    # Once the indice reaches end of the string, add string if it is valid.
    def recurse(i, left, right, left_rem, right_rem):

        if i == len(s):
            if left_rem == 0 and right_rem == 0:
                res.add("".join(expr))
            return
        if right > left:
            return
        if s[i] != '(' and s[i] != ')':
            expr.append(s[i])
            recurse(i+1, left, right, left_rem, right_rem)
        else:
            if s[i] == "(":
                if left_rem > 0:
                    recurse(i+1, left, right, left_rem-1, right_rem)
                expr.append("(")
                recurse(i+1, left+1, right, left_rem, right_rem)
            else:
                if right_rem > 0:
                    recurse(i+1, left, right, left_rem, right_rem-1)
                expr.append(")")
                recurse(i+1, left, right+1, left_rem, right_rem)
        expr.pop()

    res = set()
    left, right = 0, 0
    # Count the number of unmatching left and right parentheses
    for i, c in enumerate(s):
        if c == "(":
            left += 1
        elif c == ")":
            if left > 0:
                left -= 1
            else:
                right += 1

    expr = []
    recurse(0, 0, 0, left, right)
    return list(res)

def removeInvalidParentheses2(s):


    def recurse(i, left, right, curr, left_rem):

        if ''.join(curr) in res:
            return
        if left+right > len(s)-i:
            return
        if i > len(s):
            return

        if i == len(s):
            if left == 0 and right == 0:
                res.add("".join(curr))
            return

        if s[i] == "(" and left > 0:
            recurse(i+1, left-1, right, curr, left_rem)
        elif s[i] == ")" and right > 0:
            recurse(i+1, left, right-1, curr, left_rem)

        curr.append(s[i])
        if s[i] != '(' and s[i] != ')':
            recurse(i+1, left, right, curr, left_rem)
        elif s[i] == "(":
            recurse(i+1, left, right, curr, left_rem+1)
        elif s[i] == ")" and left_rem >0:
            recurse(i+1, left, right, curr, left_rem-1)
        curr.pop()

    res = set()
    left, right = 0, 0
    # Count the number of unmatching left and right parentheses
    for i, c in enumerate(s):
        if c == "(":
            left += 1
        elif c == ")":
            if left > 0:
                left -= 1
            else:
                right += 1

    recurse(0, left, right, [], 0)
    return list(res)



if __name__ == '__main__':
    inp = "((i)"
    print(removeInvalidParentheses2(inp))
    #print(getSolution("(()()))", ")"))
    #print(findSolutions(["(()()))"], ")"))
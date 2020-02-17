


def fun(s):

    i = 0
    I = 0
    IO = 0

    for ch in s:
        if ch == 'i':
            i += 1

        if ch == 'I':
            I += 1

        if ch == 'O':
            if I>0:
                IO +=1
                I -= 1
            else:
                i -=1

        if ch == 'o':
            if i >0:
                i -=1
            else:
                I -=1

    return IO


print(fun(''))

#test_cases = int(input())
#for case in range(test_cases):
#    S = input()
#    res = fun(S)
#    print("Case #{}: {}".format(case, res))
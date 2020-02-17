



def fun(p):

    p = p.split(' ')
    perm = [int(x) for x in p]

    nums = [0 for _ in range(len(perm)+1)]
    nums[perm[0]] = 'L'
    nums[perm[1]] = 'R'

    for i in range(2, len(perm), 2):

        n1 = perm[i]
        n2 = perm[i + 1]

        if n1%2 ==0:
            if nums[n1-1] == 'L':
                nums[n1] = 'R'
                nums[n2] = 'L'
            elif nums[n1-1] == 'R':
                nums[n1] = 'L'
                nums[n2] = 'R'
        elif n1%2 ==1:
            if nums[n1+1] == 'L':
                nums[n1] = 'R'
                nums[n2] = 'L'
            elif nums[n1 + 1] == 'R':
                nums[n1] = 'L'
                nums[n2] = 'R'

        if n2 % 2 == 0:
            if nums[n2 - 1] == 'L':
                nums[n2] = 'R'
                nums[n1] = 'L'
            elif nums[n2 - 1] == 'R':
                nums[n2] = 'L'
                nums[n1] = 'R'
        elif n2 % 2 == 1:
            if nums[n2 + 1] == 'L':
                nums[n2] = 'R'
                nums[n1] = 'L'
            elif nums[n2 + 1] == 'R':
                nums[n2] = 'L'
                nums[n1] = 'R'

        if nums[n1] == 0 and nums[n2]==0:
            nums[n1]= 'L'
            nums[n2] = 'R'


    return ''.join(str(x) for x in nums[1:])


test_cases = int(input())
for case in range(test_cases):
    N = input()
    s = input()
    res = fun(s)
    print("Case #{}: {}".format(case+1, res), flush=True)
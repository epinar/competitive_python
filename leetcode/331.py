

def isValidSerialization(preorder):

    preorder = preorder.split(",")
    #print(preorder)

    cnt=1

    for i, node in enumerate(preorder):

        if cnt == 0:
            return False

        if node == "#":
            cnt-=1
        else:
            cnt+=1

    return cnt == 0



inp = "9,3,4,#,#,1,#,#,2,#,6,#,#"
inp = "1,#"
inp = "9,#,#,1"
inp = "7,2,#,2,#,#,#,6,#"
inp = "#,#,#"

print(isValidSerialization(inp))
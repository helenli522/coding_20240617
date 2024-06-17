s_dict = {}


def init_check(s, t):
    for i, char in enumerate(s):
        if char in s_dict:
            s_dict[char] += 1
        else:
            s_dict[char] = 1
    for char in t:
        if char not in s_dict:
            return -1
    return 0


def is_sub(child, parent):
    j = 0
    n = len(child)
    for i in range(n):
        flag = False
        while j < len(parent):
            if parent[j] == child[i]:
                flag = True
                break
            else:
                j += 1
        if flag is True and i == n-1:
            return True
        j += 1
    return False


def check(s, t):
    n = len(t)
    f = [[False for j in range(n)] for i in range(n)]
    for i in range(n):
        f[i][i] = True

    for leng in range(2, n):
        for i in range(0, n+1-leng):
            j = i+leng
            if is_sub(t[i:j], s):
                f[i][j-1] = True
            else:
                f[i][j-1] = False

    dp = [0 for i in range(n+1)]

    for j in range(1, n+1):
        dp[j] = j
        # [0,k-1) [k,j]
        for k in range(1, j+1):
            if f[k-1][j-1] is True and dp[k-1]+1 < dp[j]:
                dp[j] = dp[k-1]+1
    print(dp[n])


s = "xyz"
t = "xzyxz"

if init_check(s, t) == -1:
    print(-1)
else:
    check(s, t)

def min_subsequences(s, t):
    s_ptr, t_ptr = 0, 0
    count = 0
    used = [False for i in range(len(t))]

    while t_ptr < len(t):
        if s[s_ptr] == t[t_ptr]:
            t_ptr += 1
        s_ptr += 1

        if s_ptr == len(s):
            s_ptr = 0
            count += 1

        if s_ptr == 0 and t_ptr < len(t):
            if used[t_ptr] is True:
                return -1
            else:
                used[t_ptr] = True

    return count


s1, t1 = "abc", "abcbc"
s2, t2 = "abc", "acdbc"
s3, t3 = "xyz", "xzyxz"

print(min_subsequences(s1, t1))
print(min_subsequences(s2, t2))
print(min_subsequences(s3, t3))

def is_anagram(s, t):
    len_s = len(s)
    len_t = len(t)

    if len_s != len_t:
        return False

    count_t = {}
    count_s = {}

    for index in range(len_t):
        t_val = t[index]
        s_val = s[index]
        count_t[t_val] = count_t.get(t_val, 0) + 1
        count_s[s_val] = count_s.get(s_val, 0) + 1

    if count_s == count_t:
        return True
    return False


# Time O(N)
# Space O(1)

if __name__ == '__main__':
    print(is_anagram(s="cassidy", t="ydicssa"))

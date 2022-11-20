def mystery(s: list, l: int, r: int, c: int):
    if l > r:
        return c
    if r == l:
        return c + 1
    if s[l] == s[r]:
        val1 = mystery(s, l + 1, r, 0)
        val2 = mystery(s, l, r - 1, 0)
        val3 = mystery(s, l + 1, r - 1, c + 2)
        return max(val1, val2, val3)
    else:
        val1 = mystery(s, l + 1, r, 0)
        val2 = mystery(s, l, r - 1, 0)
        return max(val1, val2)

ss = 'GAGCGTAATG'

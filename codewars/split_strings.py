def solution(s):
    a = []
    try:
        for i in range(0,len(s)):
            if i % 2 == 0:
                a += [s[i] + s[i + 1]]
        return a
    except Exception:
        a += [s[i] + "_"]
        return a
print(solution("abc"))


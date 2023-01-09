def solution(n, m):
    answer = []
    j = n
    k = m
    while k != 0:
        r = j % k
        j = k
        k = r
    gcd = j
    lcm = (n * m) / gcd
    answer.append(gcd)
    answer.append(lcm)
    return answer
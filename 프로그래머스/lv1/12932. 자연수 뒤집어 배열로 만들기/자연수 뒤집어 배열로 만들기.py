def solution(n):
    answer = []
    i = 0
    while n > 0:
        answer.insert(i, n % 10)
        n = n // 10
        i = i + 1
    return answer
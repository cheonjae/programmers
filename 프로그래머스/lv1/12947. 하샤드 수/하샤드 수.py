def solution(x):
    answer = True
    sum = 0
    y = x
    while y > 0:
        sum += y % 10
        y = y // 10
    if x % sum != 0:
        answer = False
    return answer
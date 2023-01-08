def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        cnt = 1
        for j in range(1, i):
            if i % j == 0:
                cnt = cnt + 1
        if cnt % 2 == 0:
            answer = answer + i
        else:
            answer = answer - i
    return answer
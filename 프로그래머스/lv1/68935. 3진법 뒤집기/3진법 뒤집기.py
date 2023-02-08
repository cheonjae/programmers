def solution(n):
    answer = 0
    count = 1
    while True:
        if n / 3 >= 3:
            answer = answer + int(n%3) * count
            count = count * 10
            n = n / 3
        else:
            answer = answer + int(n/3) * (count*10)
            answer = answer + int(n%3) * count
            break
    answer = (int(str(answer)[::-1],3))
    return answer
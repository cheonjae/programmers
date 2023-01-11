def solution(n):
    answer = 0
    list_n = list(map(int, str(n)))
    list_n.sort(reverse=True)
    ten = 1
    for i in reversed(list_n):
        answer = answer + i * ten
        ten = ten * 10
    return answer
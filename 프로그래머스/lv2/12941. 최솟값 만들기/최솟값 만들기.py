def solution(A,B):
    answer = 0
    A_sort = sorted(A)
    B_sort = sorted(B, reverse=True)
    for a, b in zip(A_sort, B_sort):
        answer = answer + a * b
    return answer
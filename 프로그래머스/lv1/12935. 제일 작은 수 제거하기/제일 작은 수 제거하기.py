def solution(arr):
    answer = []
    answer = arr
    answer.remove(min(arr))
    if len(arr) == 0:
        answer.append(-1)
    return answer
def solution(arr1, arr2):
    answer = [[]]
    answer = arr1
    for i in range(0, len(answer)):
        for j in range(0, len(answer[0])):
            answer[i][j] = answer[i][j] + arr2[i][j]
    return answer
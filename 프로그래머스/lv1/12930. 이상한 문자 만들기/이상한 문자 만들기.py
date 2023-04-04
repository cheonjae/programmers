def solution(s):
    answer = list(s)
    count = 0
    for i in range(len(answer)):
        if answer[i] == ' ':
            count = 0
        else:
            if count % 2 == 0:
                answer[i] = answer[i].upper()
                count = count + 1
            else:
                answer[i] = answer[i].lower()
                count = count + 1
    answer = ''.join(answer)
    return answer
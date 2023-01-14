def solution(s):
    answer = True
    sum = 0
    for i in s:
        if sum == -1:
            return False
        if i == '(':
            sum = sum + 1
        else:
            sum = sum - 1
    if sum != 0:
        return False
    return True
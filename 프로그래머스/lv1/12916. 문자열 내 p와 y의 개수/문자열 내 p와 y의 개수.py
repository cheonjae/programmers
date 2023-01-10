def solution(s):
    answer = True
    p_count = 0
    y_count = 0
    for i in s:
        if i == 'p' or i == 'P':
            p_count = p_count + 1
        if i == 'y' or i == 'Y':
            y_count = y_count + 1
    if p_count != y_count:
        return False
    return True
def solution(s):
    answer = ''
    s_list = list(s)
    s_list.sort(reverse=True)
    return "".join(s_list)
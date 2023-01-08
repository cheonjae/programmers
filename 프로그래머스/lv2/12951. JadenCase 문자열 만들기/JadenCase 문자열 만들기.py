def solution(s):
    answer = ''
    s_split = s.split(" ")
    s_list = []
    for i in s_split:
        s_list.append(i.capitalize())
    answer = " ".join(s_list)
    return answer
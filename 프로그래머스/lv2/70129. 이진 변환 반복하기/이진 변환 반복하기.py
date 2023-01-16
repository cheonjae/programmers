def solution(s):
    answer = []
    zero_count = 0
    binary_count = 0
    while True:
        if s == '1':
            break
        zero_count = zero_count + s.count("0")
        s = s.replace("0","")
        s = bin(len(s))[2:]
        binary_count = binary_count + 1
    answer = [binary_count, zero_count]
    return answer
        
        
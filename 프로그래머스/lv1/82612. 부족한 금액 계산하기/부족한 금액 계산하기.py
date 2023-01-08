def solution(price, money, count):
    rate = sum([i * price for i in range(1, count+1)])
    if rate > money:
        return rate - money
    else:
        return 0
    
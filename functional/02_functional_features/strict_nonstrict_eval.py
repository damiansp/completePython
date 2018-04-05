def numbers():
    for i in range(1024):
        print('=', i)
        yield i
        

def sum_to(n):
    total = 0
    for i in numbers():
        total += i
        if i == n:
            break
    return total

print(sum_to(5))

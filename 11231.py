from math import ceil, floor

while(1):
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    res = (a-7)*(b-7) / 2
    if c == 1:
        res = ceil(res)
    else:
        res = floor(res)
    print(res)

n = int(input())

x = list(map(int,input().split()))

tsum = 0
for i in x:
    tsum += i

hsum = tsum / 2

mysum = 0
c = 0
while mysum <= hsum:
    maxx = max(x)
    mysum += maxx
    x.remove(maxx)
    c+= 1

print(c)

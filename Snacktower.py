n = int(input())
a = list(map(int,input().split()))
s = set()

for e in a:
    s.add(e)
    while n in s:
        print(n,end=" ")
        n -= 1
    print()
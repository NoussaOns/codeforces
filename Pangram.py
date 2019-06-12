n = input()

s = input().lower()
pand = True
if len(s) < 26:
    pand = False
else:
    for i in range(ord('a'), ord('z')+1):
        if chr(i) not in s:
            pand = False
            break

print("YES" if pand else "NO")
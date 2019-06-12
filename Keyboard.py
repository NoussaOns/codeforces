l1 = "qwertyuiop"
l2 = "asdfghjkl;"
l3 = "zxcvbnm,./"

t = input()
st = input()

for i in range(len(st)):
    shift = -1 if t == 'R' else 1
    if st[i] in l1:
        print(l1[l1.index(st[i]) + shift],end="")
    elif st[i] in l2:
        print(l2[l2.index(st[i]) + shift],end="")
    elif st[i] in l3:
        print(l3[l3.index(st[i]) + shift],end="")
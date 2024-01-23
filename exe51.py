p = int(input("PRIMEIRO TERMO: "))
r = int(input("RAZÃO: "))
d = p + (10-1) * r
for c in range(p,d+r,r):
    print(c);
    
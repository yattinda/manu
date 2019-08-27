a,b=map(int,input().split())

c = a + b
d = a - b
e = a * b

if c>=d and c>=e:
    print(c)
elif d>=c and d>=e:
    print(d)
elif e>=c and e>=d:
    print(e)

a = list(map(int, input().split()))

if a[0] == a[1] and a[1] == a[2]:
    print(10000 + a[0] * 1000)

elif a[0] == a[1] or a[0] == a[2] or a[1] == a[2]:
    if a[0] == a[1] or a[0] == a[2]:
        print(1000 + a[0] * 100)
    else:
        print(1000 + a[1] * 100)

else:
    print(max(a) * 100)

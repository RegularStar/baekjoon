T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())

    if N % H == 0:
        floor = H
        room = N // H
    else:
        floor = N % H
        room = N // H + 1

    print(f"{floor}{room:02d}")

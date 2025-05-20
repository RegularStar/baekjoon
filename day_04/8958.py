n = int(input())

for i in range(n):
    k = input()
    total = 0
    score = 0
    for j in range(len(k)):
        if k[j] == "O":
            score += 1
            total = total + score
        else:
            score = 0
    print(total)

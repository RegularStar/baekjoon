n=int(input())
number = list(map(int, input().split()))
v = int(input())
count =0
for i in range(n):
    if number[i]==v:
        count+=1


print(count)

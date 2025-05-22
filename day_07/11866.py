n ,k =map(int,input().split())
table =list(range(1,n+1))
stack =[]
i=0

while table:
     i =(i+k-1)%len(table)
     stack.append(table.pop(i))

print(f"<{', '.join(map(str, stack))}>")

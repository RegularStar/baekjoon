number = []

for i in range(28):
    number.append(int(input()))

missing = []

for i in range(1, 31):
    if i not in number:
        missing.append(i)

missing.sort()
print(missing[0])
print(missing[1])

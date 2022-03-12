n = int(input())
y = 0
for i in range(0, n):
    x = list(input())
    if x.count("1") >= 2:
        y += 1
print(y)
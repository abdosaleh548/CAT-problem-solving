x = 0
n = int(input())
for i in range(0, n):
    arr = input()
    if arr == "++X" or arr == "X++":
        x += 1
    elif arr == "--X" or arr == "X--":
        x -= 1
print(x)

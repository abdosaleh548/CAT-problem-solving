n = int(input())
for i in range(0, n):
    x = str(input())
    if len(x) > 10:
      y = [char for char in x if len(x) > 10]
      print(y[0]+str(len(x)-2)+y[-1])
    else:
        print(x)

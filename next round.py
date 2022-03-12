n, k = [int(x) for x in input().split(" ")]
scores = [int(x) for x in input().split(" ")]
scores.sort(reverse=True)
next_round_participants = 0
participants_list = [num for num in scores]
for i in range(0, n):
    if participants_list[i] >= scores[k-1] and participants_list[i] > 0:
        next_round_participants += 1
print(next_round_participants)

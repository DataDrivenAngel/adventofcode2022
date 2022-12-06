text = open("3.txt",'r')
input = text.read().split('\n')

priority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priority_dict = {letter: value for value, letter in enumerate(priority, 1)}
total_score  = 0

#elf buddies why would you not label your badges
group_count = 0
grouped_sacks = [[]]
for iter, sack in enumerate(input, 1):
    grouped_sacks[group_count].append(sack)
    
    if iter % 3 == 0:
        grouped_sacks.append([])
        group_count = group_count + 1

del grouped_sacks[-1]
for sacks in grouped_sacks:

    common = set(sacks[0])&set(sacks[1])&set(sacks[2])
    scores = []
    for item in common:
        scores.append(priority_dict[item])

    priority_score = sum(scores)
    total_score = total_score + priority_score


print(total_score)

# 2569 is correct!
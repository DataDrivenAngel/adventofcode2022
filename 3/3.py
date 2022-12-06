text = open("3.txt",'r')
input = text.read().split('\n')

priority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priority_dict = {letter: value for value, letter in enumerate(priority, 1)}
total_score  = 0

for  sack in input:
    # split in half
    c1 = sack[0:(len(sack)/2)]
    c2 = sack[len(sack)/2:]
    common = set(c1)&set(c2)
    scores = []
    for item in common:
        scores.append(priority_dict[item])

    priority_score = sum(scores)
    total_score = total_score + priority_score


print(total_score)

# 7763 is correct!
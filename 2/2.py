text = open("2.txt",'r')
input = text.read().split('\n')

scores ={
    "win"  : 6,
    "draw" : 3,
    "loss" : 0,
    "R"    : 1,
    "P"    : 2,
    "S"    : 3,
}

moves = {
    "A"    : "R",
    "B"    : "P",
    "C"    : "S",
    "X"    : "R",
    "Y"    : "P",
    "Z"    : "S",
}


# rock > paper > scissors > rock
# A > B > C > A
# X > Y > Z > X
# X = A
# Y = B
# Z = C

total_score = 0
for iter, rounds in enumerate(input):
    round = input[iter].split()
    elf = round[0]
    self = round[1]
    round_score = scores[moves[self]]
    status = ""

    if moves[self] == moves[elf]:
        status = "draw"
    elif moves[self] == "R" and moves[elf] == "P":
        status = "loss"
    elif moves[self] == "P" and moves[elf] == "S":
        status = "loss"
    elif moves[self] == "S" and moves[elf] == "R":
        status = "loss"
    else:
        status = "win"

    round_score = round_score + scores[status]


    total_score = total_score + round_score
   # print(iter, "|", round, "|",elf,self,"| ", "Elf played",scores[elf], " versus your", scores[self], "you", status, "| Round Score:",round_score,"Total Score:",total_score)
print(total_score)

# 10941 is correct!
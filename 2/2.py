text = open("2.txt",'r')
input = text.read().split('\n')
# scores
win = 6
draw = 3
loss = 0
shape_rock = 1
shape_paper = 2
shape_scissors = 3

# rock > paper > scissors > rock
# A > B > C > A
# X > Y > Z > X
# X = A
# Y = B
# Z = C
round = input[0].split()
elf = round[0]
self = round[1]
print(elf)


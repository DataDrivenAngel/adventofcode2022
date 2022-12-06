text = open("4.txt",'r')
input = text.read().split('\n')

# goal is to count total number of range-pairs in which either range is fully contained within another.
fully_overlapping_pairs = 0

for pair in input:
    # split into pairs and get ranges of assigned tasks per assigned pair
    # input line: "37-54,52-53"
    ass_pair = pair.split(",")
    elf0 = ass_pair[0].split("-")
    elf1 = ass_pair[1].split("-")
    SE0 = int(elf0[0])
    SE1 = int(elf1[0])
    EE0 = int(elf0[1])
    EE1 = int(elf1[1])
    
    # see if either range is inside the other.
    if (SE0 <= SE1 and EE0 >= EE1) or (SE1 <= SE0 and EE1 >= EE0):
        # SE0 ---------- EE0       OR      SE0 --- EE0
        #     SE1 -- EE1           OR  SE1 ----------- EE1

        # increment 
        fully_overlapping_pairs += 1 

print(fully_overlapping_pairs)

# 2569 is correct!
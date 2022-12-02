text = open("1.txt",'r')
input = text.read().split('\n')

# split the text into inventories per elf, as determined by new lines
# for each row, if empty, create next elf's inventory, else, add to inventory

#make list of inventory lists with starting inventory for the first elf.
inventories = [[]]

inventory_iterator = 0
for snack in input:

    inventory = inventories[inventory_iterator]
    if snack == "":
        inventories.append([])
        inventory_iterator +=1
    else:
        inventory.append(snack)


biggest_snack_sum = 0
for inventory in inventories:
    
    snack_sum = 0
    for snack in inventory:
        snack_sum += int(snack)

    if snack_sum >= biggest_snack_sum:
            biggest_snack_sum = snack_sum

#get that yummy output

print(biggest_snack_sum)

# 72511 is correct 
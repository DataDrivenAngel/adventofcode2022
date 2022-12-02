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

for elf, inventory in enumerate(inventories):
    snack_sum = 0
    for snack in inventory:
        snack_sum += int(snack)
    inventories[elf] = snack_sum

inventories.sort(reverse = True)
sum(inventories[0:3])

# 210063 is correct
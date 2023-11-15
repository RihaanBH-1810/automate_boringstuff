def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(f"{v} {k}")
        item_total += v
    print("\nTotal number of items: " + str(item_total))
def addToInventory(inventory, addedItems):
    for i in set(addedItems):
        rep = 0
        rep = addedItems.count(i)
        if i in inventory:
            inventory[i] = inventory[i] + rep 
        else:
            inventory[i] = rep
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

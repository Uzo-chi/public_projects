def displayInventory(inventory):
    """Simulate the display of a player's inventory."""
    total = 0
    print("Inventory:")
    
    for k, v in inventory.items():
        if v > 1:
            print(f"{v} {k}s")
        else:
            print(f"{v} {k}")
        total += v
            
    print(f"\nTotal number of items: {total}")
    
def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
stuff = addToInventory(stuff, dragonLoot)
displayInventory(stuff)
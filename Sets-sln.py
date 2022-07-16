#Checks if the item is already in the list
def checkShoppingList (values, item):
    if values in item : 
        return True
    else: 
        return False
#Adds to list, but it will warn if the item was already part of the list
def addToList (values, item):
    if checkShoppingList(values, item):
        print("Item already in the List")
    else:
        item.add(values)

#Create the first list
FirstList = set()
#adding items to it
addToList("banana", FirstList)
addToList("milk", FirstList)
addToList("Nutella", FirstList)
addToList("Yogurt", FirstList)
addToList("Salt", FirstList)
addToList("Oil", FirstList)
#Second list
SecondList = set()
#adding items to it
addToList("Pizza", SecondList)
addToList("Orages", SecondList)
addToList("Paper", SecondList)
addToList("milk", SecondList)
addToList("Sugar", SecondList)
addToList("Nutella", SecondList)
#Difference list and Merge
print("Element that are different in the two lists: ")
print(FirstList.difference(SecondList))
print("Final list: (two list merged)")
print(FirstList.union(SecondList))

# Element that are different in the two lists: 
# {'Salt', 'Yogurt', 'Oil', 'banana'}
# Final list: (two list merged)
# {'Yogurt', 'Salt', 'Oil', 'Sugar', 'Orages', 'banana', 'milk', 'Paper', 'Pizza', 'Nutella'}
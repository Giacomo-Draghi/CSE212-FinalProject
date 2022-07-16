# Set

Sets are used to store multiple items in a single variable, it is a great way to have a list of items. Sets have few important properties: 
1. Unordered, sets do not have a precise order unlike lists
2. Unchangeable, you can't change the value of an item once you included it on the set
3. Duplicates are not allowed

## CRUD operations in Sets

When working with Sets we can use it in different ways, but very important is to understand that we can't do all CRUD operations when working with sets, we can Create, Read and Delete, but we can't really update items in the set. 

### Create

Sets can add elements using `thisset.add("orange")`. This is done using the following sintax: 

```python
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
#{'cherry', 'apple', 'orange', 'banana'}
```
Using big O notation the performance of this operation is O(1)

### Read
If we need to read from the set, and access all the values, then we can do something like the following: 

```python
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
# banana
# cherry
# apple
```
If we want to access a specific item in the Set then we just need to specifie the value. Doing so is also a great way to check the existance of the value in the set and that is often used, the sintax would be the following:

```python
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
# True
```

### Delete
Deleting item from a set is also a simple intruction and can be done with the operation `thisset.remove("banana")`, this can be simply displayd in a code with something like this: 

```python
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
# {'cherry', 'apple'}
```
## Intersection and difference of sets
There are many different methods we can use to work with sets, that can be used like: `difference()` and `union()`

If we start working with different sets, we then want to start comparing the sets, in order to do that, we can use `difference()` operator and that return out a set with the list of differences between the set, like the following: 

```python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)

print(z)
# {'banana', 'cherry'}
```

If we wanto to merge two difference sets, we can use the `union()` method, we can use it to return a single set with the merged unique values. We could use it like it follows: 

```python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y) 

print(z)
# {'google', 'microsoft', 'cherry', 'banana', 'apple'}
```

## Example

So now, if we want to use sets, we could us a real word example, to keep it simple, we can think of a shopping list, we can see the set like it is a set of items, when adding an item to the list you want to first check if the item already exists, then once you checked you can add it. At the end of loading the entire list, you need to print the list to do your shopping: 
```python
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

#we create the shopping list
thisset = set()

#We add some items to our shopping list
addToList("banana", thisset)
addToList("milk", thisset)
addToList("banana", thisset)

#We print the list
print(thisset)
#Item already in the List
#{'banana', 'milk'}
```

## Problem Solve: Different Shopping

Now we can practive with some more difficult proble, you can think as if you had talked with your room mate and made agreement on a list of items to get on the shopping, you then add it, but you roommate also has a list of items he wants to get, you then decide to check the difference of the tow different list, you want to come with the followig operation: 

1. Create a first set and add some item to it
2. Create a second set and add items as well
3. Compare the two list and come with the list of differences
4. Come with a final list that has elements from both list, but none repeated

[Back to Homepage](Home)

You can find a solution example here: [Solution](Sets-sln.py) 
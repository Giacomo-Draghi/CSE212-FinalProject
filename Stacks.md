# Stacks

When working in Phyton you will find yourself working with stack, but what is it? Staks is a data structure that stores items with a LIFO logic (Last-in/First-Out). This kind of thinking is opposite to FIFO (First-In/First-Out).

You can think of stacks as the **Undo function**, in fact, when you use your so loved Ctrl+z to go back one action, you are just taking of the last input from the equasion (So, you are using LIFO).

You can also think of it as if you where preparing something to eat, like **tortillas**, if you want to keep the tortilla **hot** then you *need to take the last you preparet in order to eat it warm*.

## Using Stacks

When using stacks on Phyton you can go for different ways, for sake of example, we will use stacks with list. So going back to the exaple of the tortillas we just mention, we need to try to start declaring a list of tortilla. We can declare a list pretty easilly, but when adding an item to the stack we use a operatore called **Push**
### Push

Push operator, adds the value sent as argument, and puts it at the end of the stack, like piling tortillas in the plate, and it appens using `my_stack.append(value)`. This is done using the following sintax: 

```python
tortillas = []
tortillas.append(1)
tortillas.push(2)
tortillas.push(3)
```
Using big O notation the performance of this operation is O(1)

### POP
So we just now prepared 3 tortillas, if we where to pint the list we would see the totillas like so: 
```python
print(tortillas)
# [1, 2, 3]
```
Now that we made the list, we are ready to really start taking some from the plate, that is done using the **Pop** operator, and it looks a little like this `my_stack.pop()`, with a performance of O(1).

So if we start taking some tortilla from the plate we need to do this: 
```python
tortillas.pop()
tortillas.pop()
print(tortillas)
# [1]
```
And if we just keep coocking and people keeps coming to get the food, it can be rapresent with something like this: 
```python
tortillas.append(4)
tortillas.append(5)
tortillas.pop()
tortillas.append(6)
print(tortillas)
# [1, 4, 6]
```
## Properties
Some other operators that are really helpful when it comes to use stacks are the `size()` and `empty()` operators. 

When working with elements we often need to check some conditions of our variables, like with the plate of tortilla we where just talking about, if we wanted to know how many tortilla there are left on the plate, we need to use the following code: 

```python
print(len(tortillas))
#3
```
this will let us know that we still have 3 tortillas left on the plate. So the `len(my_stack)` property returns the size of the stack. 

Another question we may raise is *"Can we check if the plate is empty"* and sure we can

```python
print(len(tortillas) == 0)
#3
```

The `if len(my_stack) == 0` condition tells us if a stack is empty. 

## Example

So if we want to make another example, we can use pizza this time. Lets say that we want to make **pizza**, but we don't know how many people will come to the dinner, nor we know how much each person will eath. 
Then we want to make sure that pizza is always on the table, we choose to operate with the following rules: 
1. Pizza is sliced in 8 pices every time
2. If there is no Pizza on the table, we will make 1 pizza (so we add 8 slice)
3. Every time the Pizza slice become less then 3 we want to make an extra pizza, so we are sure to always have some extra. 

We then assume that every time we will make pizza, people will eat the warmest slices first. The our code can look something like this: 
```python
#Makes pizza function
def makePizza(list, lastSlice = 0):
    #if there is no pizza, makes the first 8 slices
    if len(list) == 0: 
        i = 0
        while i < 8: 
            list.append(i + 1)
            i += 1
    #Otherwise it was called becouse there are less then 3
    #then we need to add another 8 slices.
    else:
        lastPizza = lastSlice + 5
        i = 0
        while i < 8: 
            list.append(lastPizza + 1)
            lastPizza += 1
            i += 1
#Take pizza slice function
def takeSlice(list):
    #takes a slice
    lastSlice = list.pop()
    #if it becomes 3, then we make new slices. 
    if len(list) < 3:
        makePizza(list, lastSlice)


pizza = []
makePizza(pizza)
takeSlice(pizza)
takeSlice(pizza)
takeSlice(pizza)
takeSlice(pizza)
takeSlice(pizza)
takeSlice(pizza)
takeSlice(pizza)
takeSlice(pizza)
takeSlice(pizza)
takeSlice(pizza)
takeSlice(pizza)
takeSlice(pizza)
takeSlice(pizza)
takeSlice(pizza)
takeSlice(pizza)
print(pizza)
#[1, 2, 15, 16, 17, 18, 19, 20, 21]
```

## Problem Solve: Storage

Lets say now that you need to keep a certain item in storage. You want to make sure the items are always in stock, and you use it with a LIFO logic. 

You then want to follo the following rules: 
1. Item must be in stock, minimum 20 items
2. Reordering item must be done in multiples of 5
3. When a customer orders items, it declares the number he wants
4. if the number required is higher of the stock, we need to restock and hev enough to fulfill the order. 

So for example, if a customer comes and oders 40 items, and have just 20, we want to reorder about 40 items. If another one comes and orders 37, then we need to reorder 20 leaving us with 23 items. this logic is to be keeps for all the orders. 
Also items should have **unique values id**, it should never be repeated, and should be a growing number. 

[Back to Homepage](Home)

You can find a solution example here: [Solution](Stacks-sln.py) 
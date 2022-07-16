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
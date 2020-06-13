# Lists are python's form of ARRAY. Behave similar to array.There some imp features are:

### LISTS

# TYPES OF LISTS
mylist1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mylist2 = ['name', 'place', 'animal', 'thing']
mylist3 = [True, False]
mynextedlist = [[1, 2, 3], ['name', 'place'], [True, False]]

print('')
print(mylist1, type(mylist1))
print(mylist2, type(mylist2))
print(mylist3, type(mylist3))
print(mynextedlist, type(mynextedlist))
print(mylist1, mylist2, mylist3, mynextedlist)

print('')
# LENGHT OF LISTS
print('Length of list1: ', (len(mylist1)))
print('Length of list2 : ', len(mylist2))
print('Length of list3: ', len(mylist3))
print('Length of nexted list: ', len(mynextedlist))

# PRINTING ITEM FROM THE LIST

mylist = ['a', 'b', 'c']

print("1rd item from the list: ", mylist[0])
print("2rd item from the list: ", mylist[1])
print("3rd item from the list: ", mylist[2])

# INDEXING FROM THE LISTS
print(mylist1[::2])  # Leaving every set by no -2
print(mylist[1:])  # from first till the end
print(mylist[2:])  # from second till the end

# ASSAIGNING places in the list [IMPORTANT]
list = ['1', '2', '3', '4', '5']  # Parent list for Down CODE
print('Before assigning values')
print(list)
print('After assigning terms')
list[0] = 'new item'
print(list)
list[1] = 'new item 2'
print(list)
print('and so on')

# ADDING A NEW ITEM IN THE LIST
list = ['1', '2', '3', '4', '5']  # Parent list for Down CODE

list.append('Item added')  # This will add a new item in the list
print(list)

### Appending and extending using .append and .extend lists

# Appending/adding a new list to the list
list = ['1', '2', '3', '4', '5']  # Parent list for Down CODE

list.append(['x', 'y', 'z'])
print(list)

# one more way of doing the same
list = ['1', '2', '3', '4', '5']  # Parent list for Down CODE
addon = ['x', 'y', 'z']

list.extend(addon)  # Here addon will be now a part of the list
print(list)

## Removing something from the list
list = ['1', '2', '3', '4', '5']  # Parent list for Down CODE

list.pop()  # This will pop out the last item from the list
print(list)

list.pop(2)  # T his will remove the '3rd' item from the parent list
print(list)

# Reversing the list
list = ['1', '2', '3', '4', '5']  # Parent list for Down CODE

list.reverse()  # This will reverse out the items in the list
print(list)

# sorting the numbers in the list
list = [1, 456, 2, 132, 23, 48, 56]  # Parent list for Down CODE

list.sort()  # This will put all the numbers in the accending order
print(list)

# NEXTED List playing with list in a list
list = [1, 2, ['x', 'y', 'z']]

print(list[2])  # This will print the list
print(list[2][1])  # This will print the first item in the list inside the list
print(list.pop[2][1])  # This will pop out the item of list inside the list

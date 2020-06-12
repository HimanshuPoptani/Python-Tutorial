# Lists are python's form of ARRAY. Behave similar to array.There some imp features are:

### LISTS

#TYPES OF LISTS
mylist1 = [1,2,3,4,5,6,7,8,9]
mylist2 = ['name' , 'place' , 'animal' , 'thing']
mylist3 = [True , False]
mynextedlist = [[1,2,3] , ['name' , 'place'] , [True , False]]

print(mylist1)
print(mylist2)
print(mylist3)
print(mynextedlist)
print(mylist1 , mylist2 , mylist3 , mynextedlist)

#LENGHT OF LISTS
print('Length of list1: ' , (len(mylist1)))
print('Length of list2 : ' , len(mylist2))
print('Length of list3: ' , len(mylist3))
print('Length of nexted list: ' , len(mynextedlist))

#PRINTING ITEM FROM THE LIST
mylist = ['a','b','c']

print("1rd item from the list: " , mylist[0])
print("2rd item from the list: " , mylist[1])
print("3rd item from the list: " , mylist[2])

#INDEXING FROM THE LISTS
print(mylist1[::2])#Leaving every set by no -2


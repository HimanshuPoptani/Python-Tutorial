b = 'Himanshu POptani'
#Slicing
print(b[1])#only at no -1
print(b[1:6])#no -0 to -6
print(b[::3])#Alternating leaving every letter at no -3


###Basic Meathod

#UPPER CASE
print(b.upper())
#LOWER CASE
print(b.lower())
#CAPATILIZE
print(b.capitalize())
#SPLITING
print(b.split())
#DEFAULT SPLIT
print(b.split('a')) #It will split every letter from 'a'


###PRINT FORMATTING

###X = "Insert another string here: {}".format("INSERT ME")print (X)

#MULTIPLE STRINGS
X = "Item one: {} Item two: {}".format("'Dog'" , "'Cat'")
print(X)
#MULTIPLE STRINGS BY "ID"
x = "Item one: {itema} Item two: {itemb}".format(itemb ="'Dog'",itema ="'Cat'")
print(x)

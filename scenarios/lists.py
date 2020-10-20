#Created an empty
fruits = []

#Created a list that contains some items in the list
vegetables = [peas]

#Add an item to the end of a list
fruits.append("Apple")
fruits.append("berry")

#Add an item in the second location
fruits[0] = "banana"

#Remove an item
fruits.remove("banana")
del fruits

#Display lists
print(fruits)

def get_fruits():
  fruits = []
  for count in range(5):
    print("Please enter a fruit:")
   fruits.append(input())
 print("Your fruits are: {}".format(fruits)) #Displays items in the list
 print("Sliced: {}".format(fruits[0:2])) #Display the range of the first items
 print("Negative Index: {}".format(fruits[-1])) #Last in the list
 print("Slice with negative: {}".format(fruits[-3:-1])) #Range from the last in list
get_fruits()
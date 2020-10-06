print("ZZZ") #Displays text for the user
YYY = input() #Expects the user to enter a value and XXX is he variable for that value
print("Blah blah blah", YYY) #Allows you to input the value into dialogue
XXX = int(input()) #Reads a user input as a number
WWW = float(input)() #Floats decimal numbers or numbers for scientific notation
#-----#
print("\n") #Skips a line
print(""" / """) #Allows the dialogue to span dialogue accross multiple lines
print("\t") #Adds a tab into dialogue
print("\n\t") #Mix prenotes together
print('"XXX"') #Use single quotes to allow spoken dialogue
#-----#
if (len(YYY) > 10): #Len means 'length' of the input value
  print("This value is very long")
elif (len(YYY) > 6): #'Else If' is a way to add other declarable values to an if statement
  print("This value is longer")
else: #Only one else per if statement
  print("This value is shorter") #Without an 'else' after the if code will flow down again
#-----#
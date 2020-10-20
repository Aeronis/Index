person = ("Prins", 36) #Mixed data sets in a value
print(type(person)) #Shows the class as a tuple
print(person + (22, 46)) #Creates a new tuple

#Concatenation
double_person = person + person
print(double_person)

#Repetition
quad_person = person * 4
print(quad_person)

#Min Maxing
temperatures = (12, 13. 14)
print(min(temperatures))
print(max(temperatures))

def coords():
  return 12, 34

print(coords())
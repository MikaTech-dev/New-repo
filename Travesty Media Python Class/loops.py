# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

Jojo = ['Jonathan', 'Joseph', 'Jolynne', 'Johnny']
  
  
# Simple for loop
'''for person in Jojo:
  print(f'Current person: {person}')'''
    # For each person in the Jojo list, print each person with the prefix Current person: 
  
# Break
'''for person in Jojo:
  if person == 'Jolynne':
    break
  print(f'Current person: {person}')
    # For each person in Jojo list, check if the value IS jolynne. If it is, break out of the loop.
'''
Jojo.insert(2, 'Dio')
    # Add dio as a none joestar

# Continue to SKIP a value
'''for person in Jojo:
  if person == 'Dio':
    print('Fake Joestar *skip*')
    continue
  print(f'Current Person {person}')
    # For each person in the Jojo list, if we (the code) runs into a char 'Dio', Mention that hes not a real Joestar, skip him and print the remaining char in the list
'''

# range
'''for i in range(len(Jojo)):
  print(Jojo[i])
  # we basically assigning everything within the length and range of the Jojo list to variable 'i' then printing Jojo list sequencially, vertically
  
for i in range(len(Jojo)):
  print(Jojo, {i})
  # Printing Jojo list as many times as the length of the list, the number of values in the list, starting from zero
  
for i in range (0,11):
  print(f'Numbers: {i}')
    # This loop will KEEP printing numbers starting from zero till it has printed 11 integers. 
    # We've assigned the range of integers 0-11 to i, so when we print i in an embedded dict
'''

# While loops execute a set of statements as long as a condition is true.

count = 0
while count <=5:
  print(f'Count: {count}')
  count +=1
# Declare variable, assign balue to variable, while count is less or equal to 5, print count. if count isnt still less than 5, plus 1 till it is

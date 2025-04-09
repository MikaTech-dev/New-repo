# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')

# Using a constructor
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs trailing comma
fruits2 = ('Apples',)

# Get value
print(fruits[1])

# Can't change value
# fruits[0] = 'Pears'

# Delete tuple
del fruits2

# Get length
print(len(fruits))


# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')

# Remove from set
fruits_set.remove('Grape')

# Add duplicate
fruits_set.add('Apples')

# Clear set
fruits_set.clear()

# Delete
del fruits_set

# print(fruits_set)


# you didnt get taught this but you can actually add tuples together
# Would be useful if you needed to check if something is in in multiple tuples.
# would look something like
Water = ('Oxygen, ' 'Hydrogen, ')
forgot_Something = ('And another Hydrogen molecule')
Total = Water + forgot_Something
print (Total)

# if you wanted to add SETS together on the other hand, type in | between the name of each set, or name the first set, add the .union function and list the remaining sets like so
# Just remember sets are unordered, that's basically what makes them better/faster for retrieving data in large databases i reckon. it also spits out the information within itself 
water1 = {'oxygen' 'Hydrogen'}
forgot_Something1 = {'another hydrogen molecule'}
Total1 = water1 | forgot_Something1
# or Total1 = water1.union (forgot_Something1)
# Just now finding out sets in python are just like their mathematical counterparts. you can union (| or .union) intersect (& or .intersection) and differentiate (- or .difference)
print (Total1)
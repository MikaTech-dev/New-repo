import os
os.system('cls' if os.name == 'nt' else 'clear')

# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create dict
thisperson = {
    'firstname': 'James', 
    'lastname': 'Bond', 
    'age': 30 
    }

#making it vertical makes it more legible and readable to humans than horizontal cause that looks clumped ykwim

            ##print(person, type(person))

# To Get a value from within the dictionary;
    #You could use the get function
print('(First Get)', thisperson.get('firstname'))

        #OR
    # Open a bracket

print('(Second Get)', thisperson['lastname'])

# You can also add stuff to it
    # REMEBMER No duplicate members

thisperson['phone_no'] = '0906-054-0096'
'''print('dict with phn no', [person])
'''

# Get dictionary keys
print('THIS PERSON KEYS', thisperson.keys())
# Prints only the keys and NOT the values


# You can also print the items
print('THIS PERSON ITEMS',thisperson.items())

# You can COPY dictionaries as well
thatperson = thisperson.copy()
thatperson['city'] = 'Canada'
print('THAT PERSON ITEMS: ', thatperson.items())

'''
ABOVE WE made a DUPLICATE of "this person" and named the duplicate diictionary THAT PERSON. We then added a new key 
and value (City and Canada) and printed only the items of dict THATPERSON
'''



# You can DELETE stuff as well with the del or .pop functions

#del(thisperson['age'])
thisperson.pop('phone_no')
print(thisperson)


# We can also CLEAR a dictionary with the .clear function, meaning thus on, if we print that variable, it will yield an empty dictionary

thisperson.clear()
print(thisperson)

# Witness that the empty dictionary prints as {}


# We can get length of a dictionary by embedding the len() into the print(). I.E:
print(len(thatperson))

# See that the length is 5 because there are 5 pairs of keys and values in THATPERSON
#printing the empty dictionary will return zero
print(len(thisperson))

'''
thisperson['My name'] = 'Jeff'
print(thisperson, type())
    We could decide to add to the empty dict by saying the above. Always remember to add in the BRACKETS`
'''

# Make a LIST with multiple dictionaries

TheJOJOs = [
    {'firstName': 'Joseph', 'lastName': 'Joestar', 'Age': 48, 'Relationship': 'Father'},
    {'firstName': 'Jonathan', 'lastName': 'Joestar', 'Age': 28, 'Relationship': 'Father'},
    {'firstName': 'Jolyne', 'lastName': 'Joestar', 'Age': 17, 'Relationship': 'GrandDaughter'}
]

print(TheJOJOs)
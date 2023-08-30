
'''import turtle


bicycles = ['trek', 'cannodae', 'redline', 'specialised']


#Remove trek
#print(bicycles)
bicycles.remove('trek')
#print(bicycles)
# Remove ast element(specialized)
del bicycles[-1]
#print(bicycles)

invitees = ["Natalien", "Brian", "Natalia", "Joy", 'Bakang' ]

print("Dear",invitees[0],"This invitation card invites you to my party")
print("Dear",invitees[1],"I would like you to join my party")
print("Dear",invitees[2],"Time was cut too short, but we can still make up for it. Join me in my party")
print("Dear",invitees[3],"I can't have a party without your smile around, come and lighten the party")
print("Dear",invitees[4],"Come around\n\n")

print(invitees[4])
invitees[4] = 'Thabiso'

print("Dear",invitees[0],"This invitation card invites you to my party")
print("Dear",invitees[1],"I would like you to join my party")
print("Dear",invitees[2],"Time was cut too short, but we can still make up for it. Join me in my party")
print("Dear",invitees[3],"I can't have a party without your smile around, come and lighten the party")
print("Dear",invitees[4],"Come around\n\n")
print("I found a new table")

#Adding more invitees
invitees.insert(5,"Thabang")
invitees.insert(6,"Mpho")
invitees.insert(7,"Sefiwa")
invitees.insert(8,"Jessica")
invitees.append("Lame")
print(invitees)

#Removing the last invitee
invitees.pop()
print(invitees)

# Removing all but two invitees
for invitee in range(len(invitees) - 2):
    removed = invitees.pop()
    print("Sorry dear",removed,"I can't invite you to my party")
print(invitees,"\n\n")

# Sending messages to remaining two invitees
for invitee in range(len(invitees)):
    print("Dear",invitees[invitee],"You're still invited to my party")


del invitees[0]
del invitees[-1]
print(invitees)

cars = ['bmw', 'subaru', 'audi', 'nissan', 'toyota']

for car in range(len(cars)):
    if len(cars[car]) < 5:
       cars[car] = cars[car].upper()
    else:+
       cars[car] = cars[car].capitalize()

print(cars)
print(sorted(cars))
print(cars)
cars.sort(reverse=True)
cars.reverse()
print(cars)

#Exercise 3.8
#Places I would like to visit
places = ['Silicon Valley', 'Madrid', 'London', 'Tokyo', 'Beijin']
print(places)
print(sorted(places))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.extend(['Gabs','Ramotswa','Joburg'])
print(places)
print(places.count('Tokyo'))

'''


'''wn = turtle.Screen()

alex = turtle.Turtle()
alex.forward(80)
alex.left(90)
alex.backward(-80)


wn.mainloop()

tup1 = (1,3,6)
print(type(tup1))
tup2 = tup1 + ("hello", 2022,(9,10))
print(tup2)
print(tup2[4])
print(2022 in tup2)
print(min(tup1))
print(max(tup1))
mine = [1,2,3,4,5,6]
print(tuple(mine))
asd = tuple(mine)
print(asd.count(1))
print(asd.index(1))
'''

# Sets
a_set = {}
print(type(a_set))
a_set = set()
print(type(a_set))
a_set.add(1)
print(a_set)
a_set.update({1, 1, 1, 3, 5, 7})
print(a_set)
if 1 in a_set:
    a_set.discard(1)
    print('1 is deleted')
    print(a_set)
else:
    print('1 is not found')
    print(a_set)

if 1 in a_set:
    a_set.discard(1)
    print('1 is deleted')
    print(a_set)
else:
    print('1 is not found')
    print(a_set)

# Take two sets
set4 = set(['Hello Python!', 3.14, 1.618, 'Hello World!'])
set5 = set([3.14, 1.618, True, False, 2022])
# Printing two sets

print(set4, set5)
print(set4 & set5)
print(set4.intersection(set5))

A = [1,1,2,2,3,3,4,4,5,5] # Take a list
B = {1,1,2,2,3,3,4,4,5,5} # Take a set
print('The minimum number of A is', min(A))
print('The minimum number of B is', min(B))
print('The maximum number of A is', max(A))
print('The maximum number of B is', max(B))
print('The sum of A is', sum(A))
print('The sum of B is', sum(B))

set8 = {1,3,5,7,9}
print(set8)
set9 = set8
print(set9)
set8.add(11)
print(set8)
print(set9)
set9.add(14)
print(set8)
print(set9)

#copy() function
#it returns a shallow copy of the original set.
"""
When this function is used, the original set stays unmodified.
A new copy stored in another set of memory locations is created.
The change made in one copy won't reflect in another.
"""
set8 = {1,3,5,7,9}
print(set8)
set9 = set8.copy()
print(set9)
set8.add(11)
print(set8)
print(set9)

#clear() function
#it removes all elements in the set and then do the set empty.
#pop() function
#It removes and returns an arbitrary set element.
x = {0, 1,1,2,3,5,8,13,21,34}
print(x)
x.pop()
print(x)
x.pop()
print(x)
x.pop()
print(x)
x.pop()
print(x)




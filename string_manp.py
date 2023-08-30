
# String manipulation
fox = "tHe qUICk bROWn fOx."
#To convert the entire string into uppercase or lowercase
fox.upper()

# Out [4]: 'THE QUICK BROWN FOX.'
fox.lower()
# Out [5]: 'the quick brown fox.'

#A common formatting need is to capitalize just the first letter of
#each word, or perhaps the first letter of each sentence. This can be
#done with the title() and capitalize() methods:
fox.title()
#Out [6]: 'The Quick Brown Fox.'

fox.capitalize()
#Out [7]: 'The quick brown fox.'

#The cases can be swapped using the swapcase() method:
fox.swapcase()
#Out [8]: 'ThE QuicK BrowN FoX.'

line = '  this is the content   '
line_1 = 'm'
print(line.strip())
print(line.lstrip())
print(line.rstrip())
print(len(line))
print(line.ljust(27, "0"))
print(line.rjust(27, "0"))
print('435'.rjust(10, '0'))
print(line_1.rjust(3, 'a'))

line_3 = 'the quick dark fox jumped over a lazy dawg'
print(line_3)

if line_3.startswith('the'):
    line_3 = line_3.capitalize()
    print(line_3)

line_2 = line_3.replace('dark', 'brown')
print(line_2)

if line_3.endswith('dog'):
    print("It's okay")
    line_3 = line_2
else:
    temp = line_2.split()
    temp[-1] = 'dog'
    line_3 = ' '.join(temp)

print(line_3)


#The partition() method returns a tuple with three elements: the
#ubstring before the first instance of the split-point, the split-point
#itself, and the substring after:

# Reading the txt file



f = open('friends_emails.txt', 'r') 
'''for line in f.readlines():
    print(line, end = '')'''


line = f.readlines()
print(line)
f.close()

line.sort()
g = open('friends_list.txt', 'w+')
for lines in line:
    g.write(lines)
    print(g.readline())
g.close()

def filter(oldfile, newfile):
    infile = open(oldfile, "r")
    outfile = open(newfile, "w")
    while True:
        text = infile.readline()
        if len(text) == 0:
            break
        if text[0] == "#":
            continue
    # Put any more processing logic here
    outfile.write(text)
    infile.close()
    outfile.close()

#filter(iter.py, iter_1.txt)
"""pi = 3.14159
r = input("What i the radius: ")
r = float(r)
area = pi * r**2
print("Area is {} ".format(area))

total_seconds = int(input("Enter seconds more than 5000: "))
hours = int(total_seconds / 3600)
remaining_seconds = int(total_seconds % 3600)
minutes = int(remaining_seconds / 60)
seconds = int(remaining_seconds % 60)

print("time is",hours,":",minutes,":",seconds)
'''
'''
time = int(input('enter time:'))
add_hours = int(input('Enter hours to wake up after:'))
total = time + add_hours
days_pass = (total) // 24
time = total % 24
print("time is",time)#'hrs','after',days_pass, "days")

print("python/'s genious")
print('''Albert Einstein once said,
"A person who never made a mistake never tried anything new."''')
name = " Monametsi Seele "
print(name)
print(name.strip())
print(name.lstrip())
print(name.rstrip())

x = 12.0
y = 15.9
y = round(y)

print(str(x+y))
"""
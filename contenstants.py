'''def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

contenstants_list = []

# This is an infinite loop with middle exits!
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    if f_name == "":
        break 
    l_name = input("Last name: ")
    if l_name == "":
        break
    formatted_name = get_formatted_name(f_name, l_name)
    contenstants_list.append(formatted_name)

count = 1 
for name in contenstants_list:
    print(f"Contestant number {count} is {name} ")
    count += 1
'''

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
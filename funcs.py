def shirt_size(size='large', message="I love python"):
    print(f"T-shirt of size {size} ordered and written {message}\n")

# Calling function using ositional arguments
print("Function called using positional arguments")
shirt_size('12', "I am a winner")

# Calling function using Keyword arguments
print("Function called using keyword arguments")
shirt_size(message="I have won", size="medium")

shirt_size('large')
shirt_size(size='small')
shirt_size(size='x-small', message="I love Jesus")

#Adding an optional argument
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
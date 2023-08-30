def mult_row(row, length):
    for i in range(1, length + 1):
        if i*row < 10:
            print(i*row, end="   ")
        elif 10 <= i*row < 100:
            print(i*row, end="  ")
        elif i*row >= 100 :
            print(i*row, end=" ")
    print()

def mult_table(length):
    for row in range(1, length + 1):
        mult_row(row, length)

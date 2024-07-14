#i
def print_average(x, y):
    average = (x + y) / 2
    print(f"Μέσος όρος των μεταβλητών {x} και {y} είναι: {average}")

print_average(2, 10)

#ii
def find_max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

max_value = find_max_of_three(8, 4, 6)
print(f"Η μεγαλύτερη τιμή είναι: {max_value}")

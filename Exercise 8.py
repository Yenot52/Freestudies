income = 30000  

if income <= 10000:
    tax = 0
elif income <= 20000:
    tax = (income - 10000) * 0.10
else:
    tax = (10000 * 0.10) + (income - 20000) * 0.20

print(f"The tax for an income of {income} is {tax}")
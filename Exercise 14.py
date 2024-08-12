def multiply_and_check(a, b):
    product = a * b
    if product > 1000:
        return product, a + b
    else:
        return product
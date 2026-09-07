def product_of_multiples(factor, limit):
    result = 1
    
    # Generate multiples of 'factor' starting at factor up to limit
    for num in range(factor, limit,factor):
        result *= num
        
    return result

# Multiples of 3 less than 10 are: 3, 6, 9
# Product: 3 * 6 * 9 = 162
print(product_of_multiples(3, 10))
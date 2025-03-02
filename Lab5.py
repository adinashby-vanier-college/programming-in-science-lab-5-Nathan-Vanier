# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    result = ""

    for i in range(1, n + 1):
        if i == 1 or i == n:
            result += "*" * n
        else:
            result += "*" + " " * (n -2) + "*"
        if i != n:
            result += "\n"
    return result

# 1
# 12
# 123
# 1234
def number_pattern(n):
    result = ''
    for i in range(1, n + 1):
         for j in range(1, i + 1):
             result += str(j)
         result += '\n'
    return result.strip()

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    total = 0
    i = 1

    while i <= n:
        total += i
        i += 1
    
    return total

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    result = ""

    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "*" * (2 * i - 1)
        
        if i == n:
            result += spaces + stars 
        else:
            result += spaces + stars + "\n"

    return result
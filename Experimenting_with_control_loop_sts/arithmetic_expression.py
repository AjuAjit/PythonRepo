import math     # math is imported to use square root, sin, pi and e


# prints the result of the arithmetic expression
def arithmetic_expression():
    result = 0  # result is initialized to 0
    result = 2**2 + (22/7 * math.sqrt(169))**2 + math.sin(math.pi/2) + math.exp(math.pi)
    print("Result = {0}".format(result))


arithmetic_expression()

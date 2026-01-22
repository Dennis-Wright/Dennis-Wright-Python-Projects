import logging

def add(*args):
        total = 0
        for arg in args:
            total += arg
        return total
# End function

def subtract(*args):
    total = args[0]
    for arg in args[1:]:
        total -= arg
    return total
# End function

def multiply(*args):
    total = args[0]
    for arg in args[1:]:
        total *= arg
    return total
# End function

def divide(*args):
    total = args[0]
    for arg in args[1:]:
        total /= arg
    return total
# End function

def calculate_expression(expression):   
    numbers = []
    operators = []
    current_number = ""
    
    # Parse numbers and operators
    for char in expression:
        if char in "+-*/":
            numbers.append(float(current_number))
            operators.append(char)
            current_number = ""
        else:
            current_number += char
    numbers.append(float(current_number))
    
    # Handle * and / first (bodmas)
    index = 0
    while index < len(operators):
        if operators[index] == '*':
            numbers[index] = multiply(numbers[index], numbers[index + 1])
            numbers.pop(index + 1)
            operators.pop(index)
        elif operators[index] == '/':
            numbers[index] = divide(numbers[index], numbers[index + 1])
            numbers.pop(index + 1)
            operators.pop(index)
        else:
            index += 1
    
    # Handle + and - next
    result = numbers[0]
    for i, operator in enumerate(operators):
        if operator == '+':
            result = add(result, numbers[i + 1])
        elif operator == '-':
            result = subtract(result, numbers[i + 1])
    
    result_well = display_well(result)

    return result_well
# End function

def display_well(result):
    try:
        num = float(result)

        num = round(num, 6)

        if num == int(num):
            num = int(num)

        logging.info(f"Backend.py - Formatting successful, sending {num} to frontend.")

        return str(num)
    except Exception as e:
        logging.error(f"Backend.py - Error in formatting. '{e}'")
# End function

def main(expression):
    return calculate_expression(expression)
# End function

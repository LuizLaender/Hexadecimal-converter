def hex_to_decimal(hex_string):
    decimal_number = 0
    hex_string = hex_string.upper()

    for digit in hex_string:
        if '0' <= digit <= '9':
            decimal_number = decimal_number * 16 + int(digit)
        elif 'A' <= digit <= 'F':
            decimal_number = decimal_number * 16 + ord(digit) - ord('A') + 10
        else:
            return "Invalid hexadecimal input"

    return decimal_number

hexadecimal_input = input("Enter a hexadecimal number: ")

decimal_result = hex_to_decimal(hexadecimal_input)
print(f"Decimal equivalent: {decimal_result}")

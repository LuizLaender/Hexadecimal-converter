def decimal_to_hexadecimal_converter(user_input):
    hexadecimal_digits = "0123456789ABCDEF"

    if user_input == 0:
        return "0x0"

    hexadecimal = ""
    while user_input > 0:
        remainder = user_input % 16
        hexadecimal = hexadecimal_digits[remainder] + hexadecimal
        user_input //= 16

    return "0x" + hexadecimal

user_input = int(input("Enter a decimal number: "))
final_result = decimal_to_hexadecimal_converter(user_input)
print(final_result)

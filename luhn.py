def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    
    return total % 10 == 0

def main():
    card_number1 = '4111-1111-4555-1142'
    card_number2 = '4111-1111-4555-1143'

    card_translation = str.maketrans({'-': '', ' ': ''})

    translated_card_number1 = card_number1.translate(card_translation)
    translated_card_number2 = card_number2.translate(card_translation)

    if verify_card_number(translated_card_number1):
        print('VALID! for 1')
    else:
        print('INVALID! for 1')
    
    if verify_card_number(translated_card_number2):
        print('VALID! for 2')
    else:
        print('INVALID! for 2')

main()
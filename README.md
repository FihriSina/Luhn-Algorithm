# Luhn Algorithm - Card Number Validation

This project implements the **Luhn Algorithm** to validate credit card numbers. The Luhn Algorithm is a simple checksum formula used to validate various identification numbers, such as credit card numbers.

### Purpose

The purpose of this project is to demonstrate the Luhn Algorithm’s implementation in Python. The algorithm helps determine whether a given credit card number is valid or not.

### How It Works

- The algorithm reverses the digits of the credit card number.
- It then separates the digits into odd and even positions.
- For odd-position digits, it simply sums them up.
- For even-position digits, it doubles each number and adds the digits of the result if the doubled number is greater than 9.
- The final sum of both odd and even digits is checked for divisibility by 10. If it’s divisible by 10, the card number is considered valid.

### Installation

You can clone this repository and run the Python file directly:

```bash
git clone https://github.com/FihriSina/Luhn-Algorithm.git
cd Luhn-Algorithm
python luhn.py
```

### Code Overview

```python
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
```

### Example

```plaintext
VALID! for 1
INVALID! for 2
```

In this example, the first card number is valid, while the second card number is invalid based on the Luhn check.

### Acknowledgements

This solution was inspired by a FreeCodeCamp challenge, which I solved as part of their algorithm practice series.




# Luhn Algoritması - Kart Numarası Doğrulama

Bu proje, **Luhn Algoritması**'nı kullanarak kredi kartı numaralarını doğrulayan bir Python uygulamasıdır. Luhn Algoritması, çeşitli kimlik numaralarını doğrulamak için kullanılan basit bir kontrol formülüdür, özellikle kredi kartı numaraları için yaygın olarak kullanılır.

### Amacı

Bu projenin amacı, Luhn Algoritması'nın Python dilinde nasıl uygulanacağını göstermektir. Algoritma, verilen bir kredi kartı numarasının geçerli olup olmadığını belirlemeye yardımcı olur.

### Çalışma Prensibi

- Algoritma, kredi kartı numarasının rakamlarını ters çevirir.
- Ardından rakamları tek ve çift konumlara ayırır.
- Tek pozisyondaki rakamları toplar.
- Çift pozisyondaki rakamları ikiyle çarpar ve eğer sayı 10 veya daha büyükse, bu sayının rakamlarının toplamını alır.
- Tek ve çift rakamların toplamı, 10'a bölünüp bölünmediğine bakılır. Eğer 10'a tam bölünebiliyorsa, kart numarası geçerlidir.

### Kurulum

Bu repository'yi klonlayarak Python dosyasını doğrudan çalıştırabilirsiniz:

```bash
git clone https://github.com/FihriSina/Luhn-Algorithm.git
cd Luhn-Algorithm
python luhn.py
```

### Kodun Özeti

```python
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
```

### Örnek

```plaintext
VALID! for 1
INVALID! for 2
```

Bu örnekte, ilk kart numarası geçerli iken, ikinci kart numarası Luhn kontrolüne göre geçersizdir.

### Teşekkürler

Bu çözüm, FreeCodeCamp’in algoritma pratikleri serisinin bir parçası olarak çözdüğüm bir görevden alınmıştır.

import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
ambiguous_symbols = 'il1Lo0O'
chars = ''
count_chars = 0
all_symbol_for_finish_pass = ''


def yes_no_check(question):
    while True:
        print(question, end=' ')
        answer = str(input())
        if answer[0] not in ('д', 'н', 'l', 'y'):
            print('Введен некорректный ответ (водите "да" или "нет"! )')
            continue
        elif answer[0] in ('д', 'н', 'l', 'y'):
            return answer


while True:
    try:
        count_of_passwords = abs(int(input('Сколько паролей генерировать?')))
        len_of_password = abs(int(input('Какова длина одного пароля, она не может быть меньше 6 символов')))
        if count_of_passwords == int(count_of_passwords) and len_of_password == int(len_of_password):
            break
    except ValueError:
        print('Вы ввели буквы при наборе, просьба вводить ответ числами')
try:
    if len_of_password in range(0, 6) and len_of_password in range(20):
        print('Длинна паролья не может быть менее 6 символов и больше 20')
        while len_of_password in range(0, 6) and len_of_password in range(20):
            len_of_password = abs(int(input(
                'Повторюсь что, нужно ввести длину пароля от 6 до 20 символов и не нужно использовать буквы')))
except ValueError:
    print(
        'К сожалению были использованы буквы и программа не может больше продолжать работать, вы можете повторно в '
        'нее зайти при необходимости')
    exit()

answer_digits = yes_no_check('Включать ли цифры 0123456789?')
answer_lowercase_letters = yes_no_check('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?')
answer_uppercase_letters = yes_no_check('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?')
answer_punctuation = yes_no_check('Включать ли символы !#$%&*+-=?@^_ ?')
answer_ambiguous_symbols = yes_no_check('Исключать ли неоднозначные символы il1Lo0O?')
for _ in range(1, count_of_passwords + 1):
    if answer_ambiguous_symbols.lower()[0] == 'д' or answer_ambiguous_symbols.lower()[0] == 'l':
        digits = digits.translate({ord('0'): None})
        digits = digits.translate({ord('1'): None})
        lowercase_letters = lowercase_letters.translate({ord('l'): None})
        lowercase_letters = lowercase_letters.translate({ord('i'): None})
        lowercase_letters = lowercase_letters.translate({ord('o'): None})
        uppercase_letters = uppercase_letters.translate({ord('O'): None})
        uppercase_letters = uppercase_letters.translate({ord('L'): None})
    if answer_digits.lower()[0] == 'д' or answer_digits.lower()[0] == 'l':
        chars += random.choice(digits)
        count_chars += 1
        all_symbol_for_finish_pass += digits
    if answer_lowercase_letters.lower()[0] == 'д' or answer_lowercase_letters.lower()[0] == 'l':
        chars += random.choice(lowercase_letters)
    count_chars += 1
    all_symbol_for_finish_pass += lowercase_letters
    if answer_uppercase_letters.lower()[0] == 'д' or answer_uppercase_letters.lower()[0] == 'l':
        chars += random.choice(uppercase_letters)
        count_chars += 1
        all_symbol_for_finish_pass += uppercase_letters
    if answer_punctuation.lower()[0] == 'д' or answer_punctuation.lower()[0] == 'l':
        chars += random.choice(punctuation)
    count_chars += 1
    all_symbol_for_finish_pass += punctuation
    for i in range(1, len_of_password - count_chars + 1):
        chars += random.choice(all_symbol_for_finish_pass)
    print(chars)
    chars = ''
    count_chars = 0
    all_symbol_for_finish_pass = ''

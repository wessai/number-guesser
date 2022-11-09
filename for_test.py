from random import *

print('Добро пожаловать в числовую угадайку')
answer = input('Если хотите сыграть нужно написать да, если придёте позже, то нет')
if answer.lower().lstrip()[0] == 'н' or answer.lower().lstrip()[0] == 'y':
    print('Это грустно, но ничего страшного, увидимся позже!')
    exit()
elif answer.lower().lstrip()[0] == 'д' or answer.lower().lstrip()[0] == 'l':
    print('''А сейчас о правилах ,я загадываю число в диапазоне от 1 до 30 - тебе нужно его отгадать
Чем меньше меня понимать, тем больше проблем :>
Удачи!''')

else:
    print('К сожалению не понятно, что ответили, но игра не будет продолжена')
    exit()


def is_valid(s):
    if s.isdigit() and 1 <= int(s) <= 30:
        return True
    else:
        return False


random_num = randint(1, 30)
attempt_answer = 0
while True:
    try:
        answer_on_count = int(input('Теперь, введите количество попыток которые хотите, но не более 10'))
        if answer_on_count == int(answer_on_count):
            break
    except ValueError:
        print('Вы ввели буквы при наборе, просьба вводить ответ числами')
try:
    if answer_on_count not in range(1, 10 + 1):
        print('Издеваться над игрой не очень хорошо, я же сказала, что попыток не может быть больше 10 и меньше 1')
        while answer_on_count not in range(1, 10 + 1):
            answer_on_count = int(input('Давай попробуем снова, не люблю когда не слушают меня, поэтому повторю ещё '
                                        'раз, количество попыток не может быть больше 10 или меньше 1'))
except ValueError:
    print('У машины тоже есть чувства, теперь я точно обиделась, если захочешь нормально играть, заходи снова :c')
    exit()
try:
    for i in range(1, answer_on_count + 1):
        num_player = input('Введите число от 1 до 30 и проверьте удачу на день')
        if not is_valid(num_player):
            print('А я предупреждала, ответ был больше 30 или меньше 1,поэтому стало на одну попытку меньше')
            continue
        num_player = int(num_player)
        if num_player < random_num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            continue
        if num_player > random_num:
            print('Ваше число больше загаданного, попробуйте еще разок')
            continue
        if num_player == random_num:
            print(f'''Вы угадали, можно идти в казино!
        Вы угадали с {attempt_answer} попытки!''')
            break
except ValueError:
    print('У машины тоже есть чувства, теперь я точно обиделась, если захочешь нормально играть, заходи снова :c')
print('У удачи сегодня много вопросов к вам -.-')
print("Будет время - заходи")

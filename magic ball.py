import random
import time


def program():
    print('Устанавливаю связь с космосом')
    time.sleep(1)
    print('Напрягаю извилины')
    time.sleep(1)
    print('Ответ почти готов')
    time.sleep(1)
    print('Ох.....')
    time.sleep(1)


answers = ['бесспорно', 'никаких сомнений', 'определённо да', 'можешь быть уверен(а) в этом',
           'мне кажется - да', 'вероятнее всего', 'хорошие перспективы', 'знаки говорят - да', 'да',
           'пока неясно, попробуй снова', 'спроси позже', 'лучше не рассказывать', 'сейчас нельзя предсказать',
           'даже не думай', 'мой ответ - нет', 'по моим данным - нет',
           'перспективы не очень хорошие', 'сомнительно']
answers_continuation = ['Конечно ты ответишь да, я же умный', 'Отлично, давай продолжим', 'Даже не сомневался',
                        'Так уж и быть, выделю тебе немного времени',
                        'Если честно я сейчас занят, но на пару вопросов отвечу']
print('Я магический шар, и я знаю ответ на любой твой вопрос')
name_user = input('Как тебя зовут')
print(f'Привет {name_user.capitalize()}!')
time.sleep(0.6)
flag = True
while flag:
    question = input('Напиши вопрос на который хочешь узнать ответ')
    program()
    print(
        f"{name_user.capitalize()}, возможно я тебя обрадую, а может нет,но ответ - это {random.choice(answers)}")
    time.sleep(5)
    question_continuation = input("Хочешь задать ещё позадавать мне вопросы, нужно отвтетить да или нет?:>")
    if question_continuation.lower().lstrip()[0] == 'д' or question_continuation.lower().lstrip()[0] == 'l':
        print(random.choice(answers_continuation))
        continue
    elif question_continuation.lower().lstrip()[0] == 'н' or question_continuation.lower().lstrip()[0] == 'y':
        print('Жду твоего возвращения!')
        flag = False
    else:
        print('Я не разобрал,просто закончим на этом :c')
        exit()

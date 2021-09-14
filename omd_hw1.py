def step2_umbrella():
    print('А ты видел(а) дождь в прогнозе погоды на сегодня?')
    option_step2_yes = ''
    options_step2_yes = ['да', 'нет', 'не знаю']
    while option_step2_yes not in options_step2_yes:
        print('Выберите: {}/{}/{}'.format(*options_step2_yes))
        option_step2_yes = input()
    if option_step2_yes == 'да':
        print('Тогда, конечно, лучше взять')
    elif option_step2_yes == 'нет':
        print('Не бери!')
        step2_no_umbrella()
    else:
        print('Тогда посмотри прогноз погоды и ответь на мой вопрос еще раз')
        step2_umbrella()


def step2_no_umbrella():
    print('Но это её любимый зонтик, она без него никуда не ходит. Может всё-таки взять?')
    option_step2_no = ''
    options_step2_no = ['да', 'нет']
    while option_step2_no not in options_step2_no:
        print('Выберите: {}/{}'.format(*options_step2_no))
        option_step2_no = input()
    if option_step2_no == 'да':
        print('Спасибо! Теперь утка может выпить в баре')
    else:
        print('Эхх, тогда утке придется остаться дома:(')


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    else:
        return step2_no_umbrella()


if __name__ == '__main__':
    step1()

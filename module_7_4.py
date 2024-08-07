team1_num = 6
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

print('В команде Мастера кода участников %(team1_num)s!' % {'team1_num': team1_num})
print('В команде Волшебники данных участников %(team2_num)s!' % {'team2_num': team2_num})
print('Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s' % {'team1_num': team1_num,
                                                                              'team2_num': team2_num})

print('Команда Волшебники данных решила задач: {score_2}'.format(score_2=score2))
print('Волшебники данных решили задачи за {team2_time} c!'.format(team2_time=team2_time))

print(f'Команды решили {score1} и {score2} задач')

if score1 > score2 or score1 == score2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score1 < score2 or score1 == score2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'

print(f'Результат битвы: {result}')
print(
    f'Сегодня было решено {score1 + score2} задач, в среднем по {round((team1_time + team2_time) / (score1 + score2), 2)}'
    f' секунды на задачу!')

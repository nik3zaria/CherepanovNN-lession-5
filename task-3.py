tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def generating_tuples(tutors, klasses):
    for tuple in range(len(tutors)):
        if tuple < len(klasses):
            yield tutors[tuple], klasses[tuple]
        else:
            yield tutors[tuple], None


generator = generating_tuples(tutors, klasses)
print(*generator)

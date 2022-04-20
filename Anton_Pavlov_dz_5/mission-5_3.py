tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
ruk = (name for name in tutors)
klas = (klass for klass in klasses)
i = 0
while len(tutors) > i:
    if len(klasses) <= i:
        print((next(ruk), None))
        break
    print((next(ruk), next(klas)))
    i += 1

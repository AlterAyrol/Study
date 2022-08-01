def task_01():
    for i_key, i_values in students.items():
        print('ID студента - {id}, возраст студента -  {age}'.format(
            id=i_key,
            age=students[i_key]['age']
        ))

def task_2():
    all_interests = []
    all_family = 0
    for i_key, i_values in students.items():
        all_interests.append(students[i_key]['interests'])
        all_family += len(students[i_key]['surname'])
    return all_interests, all_family

students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

task_01()

interests, family = task_2()

print(f'Интересы студентов {interests}, общая длина всех фамилий студентов: {family}')





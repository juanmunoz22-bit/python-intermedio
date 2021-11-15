DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    all_python_devs = [worker['name'] for worker in DATA if worker['language'] == 'python']
    all_platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']

    adults = list(filter(lambda worker: worker['age'] > 18, DATA))
    adults = list(map(lambda worker: worker['name'], adults))
    old_people = list(map(lambda worker: worker | {'old': worker['age'] > 70}, DATA))

    all_adults = [worker for worker in DATA if worker['age'] > 18]
    all_old_people = [worker['name'] for worker in all_adults if worker['age'] > 70]
    

    python_devs = list(filter(lambda python_dev: python_dev['language'] == 'python', DATA))
    python_devs = list(map(lambda python_dev: python_dev['name'], python_devs))

    platzi_workers = list(filter(lambda platzi_worker: platzi_worker['organization'] == 'Platzi', DATA))
    platzi_workers = list(map(lambda platzi_worker: platzi_worker['name'], platzi_workers))

    for worker in all_old_people:
        print(worker)
    


if __name__ == '__main__':
    run()

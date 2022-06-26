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
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    # Imprime todos los campos de cada diciconario que cumpla la condicion
    adults = list(map(lambda worker: worker["name"], adults))
    # Sobre escribe adults y aplica map sobre cada diccionario para mostrar solo el compo name
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))
    # operador pai suma dos diccionarios,  la funcion crea un nuevo diccionaro que evalua la edad y si es
    # mayor a 70 devuelbe true y si no false, solo funciona con 3.9

    #Desafio, invertir list comprehension and high functions and viceversa
    all_python_devs2 =list(filter(lambda worker: worker['language'] == 'python', DATA))
    all_python_devs2 =list(map(lambda worker : worker['name'], all_python_devs2))

    all_platzi_workers2 = list(filter(lambda worker: worker['organization'] == 'Platzi', DATA))
    all_platzi_workers2 = list(map(lambda worker: worker['name'], all_platzi_workers2))

    adults2 = [worker['name'] for worker in DATA if worker['age'] > 18] 

    old_dictionary = lambda worker_age: worker_age > 70
    old_people2 = [worker | {'old': old_dictionary(worker['age'])} for worker in DATA]

    for worker in old_people2:
        print(worker)
    

if __name__ == '__main__':
    run()
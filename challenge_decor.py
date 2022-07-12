
def quien_es_el_man(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print('El man es German')
    return wrapper

@quien_es_el_man
def quien_es(pregunta = 'La pregunta'):
    print('La pregunta es: ' '\n'+ pregunta)
    print('La respuesta es: ')

quien_es('Quien es el man')





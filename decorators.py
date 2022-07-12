# Define el tiempo que tarda en ejecutarse una funcion y lo imprime en pantalla
from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs): # Wrapper traduce envoltura
        initial_time = datetime.now()
        func(*args, **kwargs) # *args, **kwargs es un truco para  no pasarle parametros a la nested function
        final_time = datetime.now()
        time_elapsed = final_time - initial_time # elapsed traduce transcurrido
        print('Pasaron ' + str(time_elapsed.total_seconds()) + ' segundos')
    return wrapper

@execution_time
def random_func():
    for _ in range(1, 100000000): # Con el guion bajo no se imprimem todos los ciclos
        pass  

@execution_time
def suma(a: int, b: int) -> int:
    return a + b

@execution_time
def saludo(nombre = 'Cesar'):
    print('Hola ' + nombre)

suma(5, 5)
random_func()
saludo('Alexander')



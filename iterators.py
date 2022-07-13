import time

class FiboIter():
    # las finciones iter y next son obligatorias para construir un iterador
    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.conunter = 0
        return self
        #La segunda condicion es crear los elemtos que necesito y retornar a self.



    def __next__(self):
        if self.conunter == 0:
            self.conunter += 1
            return self.n1
        elif self.conunter == 1:
            self.conunter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            #self.n1 = self.n2
            #self.n2 = self.aux
            self.n1, self.n2 = self.n2, self.aux
            # Esta linea resume las dos anteriores las cuales hacen el intercambio de valores
            #que nos permiten correr la secuencia de fibonacci
            self.conunter += 1
            return self.aux

if __name__ == "__main__":
    fibonacci = FiboIter() # Instancio la clase, queda guardada como un objeto en la variable
    for element in fibonacci:
        print(element)
        time.sleep(1)

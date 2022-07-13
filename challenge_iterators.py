from mimetypes import init
import time

class FiboIterMax():
   
    def __init__(self, max_number): # Este objeto me permite iniciar el atributo
        self.max_number = max_number

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.conunter = 0
        return self
       


    def __next__(self):
        if self.conunter == 0:
            self.conunter += 1
            return self.n1
        elif self.conunter == 1:
            self.conunter += 1
            return self.n2
        
        else:
            self.aux = self.n1 + self.n2
            if self.aux >= self.max_number:
                raise StopIteration
            self.n1, self.n2 = self.n2, self.aux
            self.conunter += 1
            return self.aux

if __name__ == "__main__":
    fibonacci = FiboIterMax(100000) 
    for element in fibonacci:
        print(element)
        time.sleep(0.05)
class EjemploExcepciones:
    # ZeroDivisionError
    def zeroDivisionError(self, *, num:int, den:int)->int:
        if (den == 0):
            raise ZeroDivisionError
        
        return num // den
    
    # ValueError
    def zeroDivisionError(self, *, num:int, den:int)->int:
        if (den == 0):
            raise ZeroDivisionError
        
        return num // den
    # FileNotFoundError
    def fileNotFoundError(self):
        x = open()
        if x != open:
            raise FileNotFoundError("No existe")
        
        return x


    # TypeError
    def typeError(self):
        


        raise TypeError

    # IndexError

    # KeyboardInterrupt no

    # UnicodeDecodeError no

    # AttributeError

    pass
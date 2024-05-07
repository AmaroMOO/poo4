import re

class RegExample:
    def __init__(self) -> None:
        pass
    @staticmethod
    def buscar(texto:str) -> None:
        #patron palabras que empiezan en vocal minuscula
        patron = "\b[aeiou][^\s.,]"
        result = re.findall(patron,texto)

    @staticmethod
    def validURL(url:str) -> bool:
        pass

    

if __name__ == "__main__":
    text = 


    print(MinVoc.buscar(text))
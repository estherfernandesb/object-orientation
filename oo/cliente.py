class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        print("chamando @property nome()")
        return self.__nome.title()
    
    @nome
    def nome(self):
        print("chamando setter nome()")
        self.__nome = nome 
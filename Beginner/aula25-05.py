
class Main():
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.apelido = "MiguelDev"
   
    def showNome(self):
        print("Welcome "+self.nome + "!")

    
    def inverterNome(self):
        #desempacotamento de tupla
        self.nome, self.apelido = self.apelido, self.nome
        return self.nome, self.apelido

miguel = Main("miguel")
miguel.showNome()
nome, apelido = miguel.inverterNome()
print(nome, apelido)


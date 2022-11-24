#Importa nosso arquivo Pessoa.py no diretorio model
from model.Pessoa import Pessoa


#Exemplo de uso
felipe = Pessoa (1, "Felipe Castro")
print(felipe)

#Quero mostrar só o nome
print(felipe.nome)


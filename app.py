import random
import string

class Tamanho_senha(Exception):
    pass

f = [
    string.punctuation[0],
    string.punctuation[2],
    string.punctuation[3],
    string.punctuation[4],
    string.punctuation[5],
    string.punctuation[20],
    string.punctuation[21],
    string.punctuation[31],
]

try:
    tamanho = int(input("Digite o tamanho da senha: "))
    if tamanho <= 0 or tamanho > 50:
        raise Tamanho_senha()
    else:
        escolhas = string.ascii_letters + string.digits + "".join(f)
        senha = "".join(random.choices(escolhas, k=tamanho))
        print(senha)
except ValueError:
    print(f'Erro: digite um número')

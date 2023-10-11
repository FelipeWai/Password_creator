import random
import string

class TamanhoSenhaInvalido(Exception):
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


def gerar_senha(tamanho):
    try:
        if tamanho <= 0 or tamanho > 50:
            raise TamanhoSenhaInvalido("Tamanho da senha deve estar entre 1 e 50.")
        
        caracteres = string.ascii_letters + string.digits + "".join(f)

        senha = "".join(random.choices(caracteres, k=tamanho))
        return senha
    except TamanhoSenhaInvalido as e:
        return f"Erro: {e}"
    except ValueError:
        return "Erro: Digite um número válido."

tamanho = int(input("Digite o tamanho da senha: "))
    
senha = gerar_senha(tamanho)
with open("passwords.txt", "a") as file:
    file.write(f"Password: {senha}, \n")
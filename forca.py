import random


def carregar_palavras():
    try:
        # Abre o arquivo e fecha automaticamente ao final do bloco
        with open("palavras.txt", "r") as arquivo:
            palavras = arquivo.readlines()
        return [palavra.strip() for palavra in palavras]
    except FileNotFoundError:
        print("Ocorreu um erro, arquivo palavras.txt não encontrado!")
        return []
    except Exception as ex:
        print(f"Ocorreu um erro: {ex}")
        return []


def escolher_palavra(palavras):
    return random.choice(palavras)


def exibir_palavra(palavra, letras_adivinhadas):
    return " ".join(
        [letra if letra in letras_adivinhadas else "_" for letra in palavra]
    )


def validar_entrada():
    while True:
        letra = input("Adivinhe uma letra: ").lower()
        if len(letra) == 1 and letra.isalpha():
            return letra
        else:
            print("Entrada inválida. Por favor, insisa apenas uma letra!")


def jogo_da_forca():
    palavras = carregar_palavras()
    if not palavras:
        return

    palavra_secreta = escolher_palavra(palavras)
    letras_adivinhadas = set()
    letras_tentadas = set()
    tentativas = 6

    print("===========================")
    print("Bem-vindo ao jogo da forca!")
    print("===========================")

    while tentativas > 0:
        print(f"\nPalavra: {exibir_palavra(palavra_secreta, letras_adivinhadas)}")

        print(f"Letras tentadas: {sorted(letras_tentadas)}")
        print(f"Tentativas restantes: {tentativas}")

        letra = validar_entrada()

        if letra not in letras_tentadas:
            letras_tentadas.add(letra)
            if letra in palavra_secreta:
                letras_adivinhadas.add(letra)
                print("\nBoa! Você adivinhou uma letra.")
            else:
                tentativas -= 1
                print("\nErrado! Tente novamente.")

            if all(letra in letras_adivinhadas for letra in palavra_secreta):
                print(f"\nParabéns! Você adivinhou a palavra: {palavra_secreta}\n")
                break
        else:
            print("\nVocê já tentou essa letra!")
    else:
        print(f"\nVocê perdeu! A palavra era: {palavra_secreta}\n")


if __name__ == "__main__":
    jogo_da_forca()

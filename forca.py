import random


def carregar_palavras():
    # Abre o arquivo e fecha automaticamente ao final do bloco
    with open("palavras.txt", "r") as arquivo:
        palavras = arquivo.readlines()
    return [palavra.strip() for palavra in palavras]


def escolher_palavra(palavras):
    return random.choice(palavras)


def exibir_palavra(palavra, letras_adivinhadas):
    return " ".join(
        [letra if letra in letras_adivinhadas else "_" for letra in palavra]
    )


def jogo_da_forca():
    palavras = carregar_palavras()
    palavra_secreta = escolher_palavra(palavras)
    letras_adivinhadas = set()
    letras_tentadas = set()
    tentativas = 6

    print("===========================")
    print("Bem-vindo ao jogo da forca!")
    print("===========================")

    while tentativas > 0:
        print(f"\nPalavra: {exibir_palavra(palavra_secreta, letras_adivinhadas)}")
        if letras_adivinhadas:
            print(f"Letras tentadas: {sorted(letras_tentadas)}")
        print(f"Tentativas restantes: {tentativas}")
        letra = input("Adivinhe uma letra: ").lower()

        if letra not in letras_tentadas:
            if letra in letras_adivinhadas:
                print("Você já adivinhou essa letra.")
                letras_tentadas.add(letra)
            elif letra in palavra_secreta:
                letras_adivinhadas.add(letra)
                print("Boa! Você adivinhou uma letra.")
                letras_tentadas.add(letra)
            else:
                tentativas -= 1
                print("Errado! Tente novamente.")
                letras_tentadas.add(letra)

            if all(letra in letras_adivinhadas for letra in palavra_secreta):
                print(f"Parabéns! Você adivinhou a palavra: {palavra_secreta}")
                break
        else:
            print("\nVocê ja tentou essa letra!")
    else:
        print(f"Você perdeu! A palavra era: {palavra_secreta}")


if __name__ == "__main__":
    jogo_da_forca()

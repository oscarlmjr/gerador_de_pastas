import os
import unidecode


with open('texto2.txt', 'r', encoding='utf8') as arquivo:

    for titulo in arquivo:
        nova_string = ''

        for caracter in titulo:
            if caracter.isalpha() or caracter.isdigit():
                nova_string += caracter
            else:
                nova_string += '_'

        nome_da_pasta = unidecode.unidecode(nova_string)
        print(nome_da_pasta)
        nome_arquivo = ".gitkeep"

        caminho_completo = os.path.join(nome_da_pasta, nome_arquivo)

        os.makedirs(nome_da_pasta, exist_ok=True)

        with open(caminho_completo, 'w', encoding='utf8') as file:
            print(nome_da_pasta)

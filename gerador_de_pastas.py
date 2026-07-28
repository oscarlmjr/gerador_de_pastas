from pathlib import Path
import os


with open('texto2.txt', 'r', encoding='utf8') as arquivo:
	
	for nova_pasta in arquivo:
		nome_da_pasta = nova_pasta.strip()
		nome_arquivo = ".gitkeep"
		caminho_completo = os.path.join(nome_da_pasta, nome_arquivo)
		
		os.makedirs(nome_da_pasta, exist_ok=True)

		with open(caminho_completo, 'w', encoding='utf8') as file:
			print(nome_da_pasta)

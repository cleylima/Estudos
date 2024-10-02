
import os
# import json
# from typing import TypedDict
#from xmlrpc.client import boolean

os.system('cls')


# class Movie(TypedDict):
   # title: str
   # original_title: str
   # is_movie: bool
   # imdb_rating: float
   # year: int
   # characters: list[str]
   # budget: None | float


#JSON
# filme = {'title': 'O Senhor dos Anéis: A Sociedade do Anel', 'original_title': 'The Lord of the Rings: The Fellowship of the Ring', 'is_movie': True, 'imdb_rating': 8.8, 'year': 2001, 'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'], 'budget': None}

# filme: Movie = json.loads(string_json)
# print(filme)
# print('')
# print(filme['title'])
# print(filme['characters'][0])

#converter em json
#json_string = (json.dumps(filme, ensure_ascii=False, indent=2))
#print(json_string)


#Trabalhando com arquivos
#informando o caminho absoluto
# Nome_Arquivo = 'principal.json'
# Caminho_absoluto_arquivo = os.path.abspath(
#    os.path.join(
#       os.path.dirname(__file__), 
#       Nome_Arquivo
#     )
# )
#criando o arquvo json
# with open(Caminho_absoluto_arquivo, 'w') as arquivo:
#    json.dump(filme, arquivo, ensure_ascii=False, indent=2)

#carregando dados do arquivo
# with open(Caminho_absoluto_arquivo, 'r') as arquivo:
#    filme_json = json.load(arquivo)
#    print(filme_json)

#________________________

#Manipulando caminho de diretório com Pathlib

# from pathlib import Path

# caminho_projeto = Path()
# print(caminho_projeto.absolute())

# caminho_arquivo = Path(__file__)
# print(caminho_arquivo)

# print(caminho_arquivo.parent)
# print(caminho_arquivo.parent.parent)
# print(caminho_arquivo.parent.parent.parent)

#_______________________


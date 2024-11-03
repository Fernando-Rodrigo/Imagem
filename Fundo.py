from rembg import remove
from PIL import Image


def removefundo():
    nome = str(input("Qual é o nome do arquivo que deseja remover o fundo? "))
    try:
        output = remove(Image.open(nome + '.jpg'))
        output.save(nome + '.png')
        print("Concluído com sucesso!!")
    except FileNotFoundError:
        print('Não foi possível remover o fundo da foto! Certifique-se de que a foto esteja no mesmo arquivo do programa.')

from PIL import Image


def imagemespelhada():
    imagem = str(input('Qual imagem deseja espelhar? '))

    try:
        # Carrega imagem original
        img = Image.open(imagem + '.jpg')

        # Espelha imagem e salva
        mirror_img = img.transpose(Image.FLIP_LEFT_RIGHT)
        mirror_img.save(imagem + 'espelhada.png')
        print('Imagem espelhada com sucesso!!')
    except FileNotFoundError:
        print('Não foi possível espelhar a imagem. Verifique se está no mesmo arquivo do programa ou se existe.')

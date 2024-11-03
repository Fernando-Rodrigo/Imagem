import Fundo
import ImagemEspelhada

opcao = int(input("0-sair\n1-remove fundo\n2-imagem espelhada\nQual a opção escolhida? "))

while opcao != 0:
    if opcao == 1:
        Fundo.removefundo()
    else:
        ImagemEspelhada.imagemespelhada()
    opcao = int(input("0-sair\n1-remove fundo\n2-imagem espelhada\nQual a opção escolhida? "))

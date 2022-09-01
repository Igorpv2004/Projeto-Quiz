from model import model

class control:
    def __init__(self):
        self.opcao = -1
        self.modelo = model()
        self.opcao1 = 0

    def getOpcao1(self):
        return self.opcao1

    def setOpcao1(self, opcao1):
        self.opcao1 = opcao1

    def getOpcao(self):
        return self.opcao

    def setOpcao(self, opcao):
        self.opcao = opcao

    def menu(self):
        print("\nEscolha uma das alternativas abaixo: "
              "\n0. Sair"  +
              "\n1. Jogar" +
              "\n2. Atualizar" +
              "\n3. Excluir")
        self.setOpcao(int(input()))

    def excluir(self):
        print("Informe o código do dado que deseja excluir: ")
        cod = int(input())
        print(self.modelo.excluir(cod))

    def menuTema(self):
        print("Escolha o tema em qual deseja jogar: \n"
              "\n1.Futebol" +
              "\n2.Música")
        self.setOpcao1(int(input()))


    def operacao(self):
        while self.getOpcao() != 0:
            self.menu()
            if self.getOpcao() == 0:
                print("Obrigado.")
                break
            elif self.getOpcao() == 1:
                self.menuTema()
                if self.getOpcao1() == 1:
                    self.jogo()
            elif self.getOpcao() == 3:
                self.excluir()

        else:
            print("Opção inválida.")

    def jogo(self):
        contador = 0
        print("Antes de começar o Quiz, informe seu nome: ")
        nome = input()
        print("1.Em que ano nasceu o Corinthians?\n"
              "\n1. 1910"
              "\n2. 1934"
              "\n3. 1951"
              "\n4. 1850")
        resposta = int(input())
        while resposta < 0 or resposta > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("1.Em que ano nasceu o Corinthians?\n"
                  "\n1. 1910" +
                  "\n2. 1934" +
                  "\n3. 1951" +
                  "\n4. 1850")
            resposta = int(input())
        if resposta == 1:
            print("Resposta Correta!")
            contador = contador + 1
        elif resposta == 2:
            print("Resposta Errada!")
        elif resposta == 3:
            print("Resposta Errada!")
        elif resposta == 4:
            print("Resposta Errada!")

        print("2.Quantos Mundiais o Palmeiras tem?\n" +
              "\n1. Nenhum" +
              "\n2. Um" +
              "\n3. Dois" +
              "\n4. Cinco")
        resposta2 = int(input())
        while resposta2 < 0 or resposta2 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("2.Quantos Mundiais o Palmeiras tem?\n" +
                  "\n1. Nenhum" +
                  "\n2. Um" +
                  "\n3. Dois" +
                  "\n4. Cinco")
            resposta2 = int(input())
        if resposta2 == 1:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta2 == 2:
            print("Resposta Errada!")
        elif resposta2 == 3:
            print("Resposta Errada!")
        elif resposta2 == 4:
            print("Resposta Errada!")

        print("3.Quantas copas do mundo o Brasil conquistou? \n" +
              "\n1. Três" +
              "\n2. Duas" +
              "\n3. Cinco" +
              "\n4. Nenhuma")
        resposta3 = int(input())
        while resposta3 < 0 or resposta3 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("3.Quantas copas do mundo o Brasil conquistou? \n" +
                  "\n1. Três" +
                  "\n2. Duas" +
                  "\n3. Cinco" +
                  "\n4. Nenhuma")
            resposta3 = int(input())
        if resposta3 == 1:
            print("Resposta errada!")
        elif resposta3 == 2:
            print("Resposta errada!")
        elif resposta3 == 3:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta3 == 4:
            print("Resposta errada!")

        print("4.Qual foi o ano em que foi em que o Brasil conquistou a última copa do mundo? \n" +
              "\n1. 1994" +
              "\n2. 1998" +
              "\n3. 2002" +
              "\n4. 2010")
        resposta4 = int(input())

        while resposta4 < 0 or resposta4 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("4.Qual foi o ano em que foi em que o Brasil conquistou a última copa do mundo? \n" +
                  "\n1. 1994" +
                  "\n2. 1998" +
                  "\n3. 2002" +
                  "\n4. 2010")
            resposta4 = int(input())
        if resposta4 == 1:
            print("Resposta errada!")
        elif resposta4 == 2:
            print("Resposta errada!")
        elif resposta4 == 3:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta4 == 4:
            print("Resposta errada!")

        print("5. Quem foi o jogador mais jovem a ganhar uma copa do mundo: \n"
              "\n1. Cristiano Ronaldo" +
              "\n2. Pelé" +
              "\n3. Messi" +
              "\n4. Neymar")
        resposta5 = int(input())
        while resposta5 < 0 or resposta5 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("5. Quem foi o jogador mais jovem a ganhar uma copa do mundo: \n"
                  "\n1. Cristiano Ronaldo" +
                  "\n2. Pelé" +
                  "\n3. Messi" +
                  "\n4. Neymar")
            resposta5 = int(input())

        if resposta5 == 1:
            print("Resposta errada!")
        elif resposta5 == 2:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta5 == 3:
            print("Resposta errada!")
        elif resposta5 == 4:
            print("Resposta errada!")




        print("sua pontuação foi: {}".format(contador))
        self.modelo.inserir(nome, contador)




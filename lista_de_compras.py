class ListaDeCompras:

    def __init__(self):
        self.lista_compras = []
        self.lista_quantidade = []

    def adicionar_itens(self, produto, quantidade):
        self.lista_compras.append(produto)
        self.lista_quantidade.append(quantidade)

    def remover_itens(self, produto):

        if len(self.lista_compras) > 0:
            try:
                para_excluir = self.lista_compras.index(produto)
                self.lista_compras.remove(self.lista_compras[para_excluir])
                self.lista_quantidade.remove(self.lista_quantidade[para_excluir])
            except ValueError:
                print('\nEste produto não está na lista!')

    def listar_itens(self):
        if self.tamanho_das_listas() > 0:

            produto = 'Produto'
            quantidade = 'Quantidade'

            print(f'\n{produto:20}     {quantidade}')

            for indice in range(len(self.lista_compras)):
                produto = self.lista_compras[indice]
                quantidade = self.lista_quantidade[indice]
                print(f'{produto:20}        {quantidade}')

        else:
            print('\nSua lista está vazia! Não há o que mostrar.')

    def tamanho_das_listas(self):
        tamanho = len(self.lista_compras)
        return tamanho


def entrada():

    resposta_valida = False

    while resposta_valida is False:
        try:
            resposta = input('Vamos começar [S/N]: ')
        except ValueError:
            pass
        else:
            if resposta == 'N':
                resposta = 'Sair'
                return resposta
            elif resposta == 'S':
                return resposta
            else:
                print('\nNão entendi a sua resposta!\n')


def controle_interface():

    comando_valido = False

    while comando_valido is False:

        try:
            comando = int(input('\nDigite [1] para adicionar itens a sua lista.\n'
                                'Digite [2] para remover itens da sua lista.\n'
                                'Digite [3] para vizualizar a sua lista.\n'
                                'Digite [4] para sair.\n'
                                'Digite o seu comando: '))
        except ValueError:
            print('\nEscolha entre os números 1 e 4.')
        else:
            if comando == 1 or comando == 2 or comando == 3 or comando == 4:
                return int(comando)
            else:
                print('\nEscolha entre os números 1 e 4.')
                comando_valido = False


Lista = ListaDeCompras()

print('\nBem-vindo(a) ao sistema criador da sua lista de compras!\n'
      'Por meio de alguns passos simples, você poderá criá-la.\n')

resp = entrada()

while resp != 'Sair':

    resp = controle_interface()

    if resp == 1:
        while True:
            item = input('\nDigite qual produto vai ser adicionado: ')
            if all(caracter.isalpha() or caracter.isspace() for caracter in item):
                break
            else:
                print('Seu nome de produto só pode conter letras ou espaços!')

        try:
            quant_item = int(input('Digite a quantidade do produto: '))
        except ValueError:
            print('Use números inteiros para adicionar a quantidade.')
        else:
            Lista.adicionar_itens(item, quant_item)

    elif resp == 2:
        if Lista.tamanho_das_listas() > 0:
            item = input('\nDigite qual item você gostaria de apagar: ')
            Lista.remover_itens(item)
        else:
            print('\nNão há o que apagar da sua lista!')
    elif resp == 3:
        Lista.listar_itens()
    else:
        resp = 'Sair'

print('\nFoi um prazer!\n')

if Lista.tamanho_das_listas() > 0:
    print('Essa é a sua lista de compras:')
    Lista.listar_itens()

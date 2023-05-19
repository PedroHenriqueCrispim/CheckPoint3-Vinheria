# Rafael Autieri - RM550885
# Caique Chargas - RM551943
# Rodrigo Resende - RM551057
# Pedro Crispim - RM99005
# Giuliano Romaneto - RM99694


# Lista de vinhos disponíveis
vinhos = {
    'ROSÉS': [
        {'nome': '1-Cabernet Franc', 'preço': 70},
        {'nome': '2-Syrah', 'preço': 80},
        {'nome': '3-Grenache', 'preço': 60}
    ],
    'TINTOS': [
        {'nome': '1-Cabernet Sauvignon', 'preço': 100},
        {'nome': '2-Pinot Noir', 'preço': 120},
        {'nome': '3-Tinto Malbec', 'preço': 80},
        {'nome': '4-Tinto Merlot', 'preço': 90},
        {'nome': '5-Tinto Syrah', 'preço': 100}
    ],
    'BRANCOS': [
        {'nome': '1-Chardonnay', 'preço': 80},
        {'nome': '2-Sauvignon Blanc', 'preço': 70},
        {'nome': '3-Riesling', 'preço': 90},
        {'nome': '4-Pinot Grigio', 'preço': 60}
    ]
}

# Carrinho de compras
carrinho = []

# Função para listar os vinhos disponíveis
def listar_vinhos():
    print('VINHOS DISPONÍVEIS:')
    for categoria, lista_vinhos in vinhos.items():
        print('\n' + categoria + ':')
        for vinho in lista_vinhos:
            print(vinho['nome'] + ' - R$' + str(vinho['preço']))

# Função para comprar vinhos
def comprar_vinhos():
    listar_vinhos()
    categoria = input('\nSelecione a categoria do vinho que deseja comprar: ')
    indice = int(input('Selecione o número do vinho que deseja comprar: ')) - 1
    quantidade = int(input('Informe a quantidade desejada: '))

    vinho_selecionado = vinhos[categoria][indice]
    item_carrinho = {
        'nome': vinho_selecionado['nome'],
        'preço': vinho_selecionado['preço'],
        'quantidade': quantidade
    }

    carrinho.append(item_carrinho)
    print('Vinho adicionado ao carrinho.')

# Função para visualizar o carrinho de compras
def visualizar_carrinho():
    if len(carrinho) == 0:
        print('O carrinho está vazio.')
    else:
        print('CARRINHO DE COMPRAS:')
        total = 0
        for item in carrinho:
            subtotal = item['preço'] * item['quantidade']
            total += subtotal
            print(item['nome'] + ' - R$' + str(item['preço']) + ' x ' + str(item['quantidade']) + ' = R$' + str(subtotal))
        print('Valor total da compra: R$' + str(total))

# Função para finalizar a compra
def finalizar_compra():
    visualizar_carrinho()
    nome = input('\nNome completo: ')
    email = input('Email: ')
    cpf = input('CPF: ')
    data_nascimento = input('Data de nascimento (DD/MM/AAAA): ')
    endereco = input('Endereço de entrega: ')


    carrinho.clear()
    print('\nCompra finalizada! Obrigado pela preferência.')

# Função principal do programa
def main():
    print('BEM-VINDO À NOSSA LOJA DE VINHOS')
    while True:
        print('\nOPÇÕES:')
        print('1 - Listar vinhos disponíveis')
        print('2 - Comprar vinhos')
        print('3 - Visualizar carrinho de compras')
        print('4 - Finalizar compra')
        print('0 - Sair')

        opcao = int(input('\nSelecione uma opção: '))
        if opcao == 1:
            listar_vinhos()
        elif opcao == 2:
            comprar_vinhos()
        elif opcao == 3:
            visualizar_carrinho()
        elif opcao == 4:
            finalizar_compra()
        elif opcao == 0:
            break
        else:
            print('Opção inválida. Tente novamente.')

# Execução do programa
if __name__ == '__main__':
    main()

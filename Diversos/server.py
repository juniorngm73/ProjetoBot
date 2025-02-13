import socket

HOST_IP = ''  # Definindo o IP do servidor
HOST_PORT = 50000  # Definindo a porta do servidor
PAGE_CODE = 'utf-8'  # Definindo o código da página

# Criando o socket TCP
socketServer = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# Ligando o servidor ao IP e porta que será "escutado"
socketServer.bind((HOST_IP, HOST_PORT))

# Tornando o socket capaz de escutar conexões
socketServer.listen(5)

print('\nServidor TCP aguardando conexões...\nPressione Ctrl+C para interromper...\n')

while True:
    try:
        # Aceitando uma conexão de cliente
        conexao, endereco_cliente = socketServer.accept()
        print(f'Conexão estabelecida com {endereco_cliente}')

        while True:
        # Enviando perguna ao Cliente
            pergunta = 'O que o comando #HOSTS faz? : '
            if pergunta.lower() =='exit':
                break
            elif pergunta:
                conexao.send(pergunta.encode(PAGE_CODE))

        # recebendo resposta do Cliente
            resposta = conexao.recv(1024)
            if not resposta:
                break
            # Se a conexao for fechada pelo Cliente
            print(f'Resposta recebida: {resposta.decode(PAGE_CODE)} de {endereco_cliente}')

            # Fechando a conexão com o cliente após a interação
            conexao.close()

            print (f'Conexão Fechada com {endereco_cliente}')

    except KeyboardInterrupt:

        print('\nServidor encerrado pelo usuário...')
        break

# Fechando o socket do servidor
socketServer.close()
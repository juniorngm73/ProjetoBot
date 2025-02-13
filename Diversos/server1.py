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

        # Enviando pergunta ao cliente
        pergunta = input('Pergunte ao Cliente: ')
        if pergunta == 'exit':
            break
        elif pergunta:
            conexao.send(pergunta.encode(PAGE_CODE))

        # Recebendo resposta do cliente
        resposta = conexao.recv(1024)
        print(f'Resposta recebida: {resposta.decode(PAGE_CODE)} de {endereco_cliente}')

        # Enviando mensagem de volta para o cliente
        mensagem_retorno = f'Ok, {resposta.decode(PAGE_CODE)}!'
        conexao.send(mensagem_retorno.encode(PAGE_CODE))

        # Fechando a conexão com o cliente após a interação
        conexao.close()
        print(f'Conexão fechada com {endereco_cliente}')

    except KeyboardInterrupt:
        print('\nServidor encerrado pelo usuário...')
        break

# Fechando o socket do servidor
socketServer.close()
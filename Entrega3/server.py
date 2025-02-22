import threading, socket, requests,function

##########################################################################
HOST_SERVER = 'localhost'
PORT = 55000
SERVER = '0.0.0.0'
CODE_PAGE = 'utf-8'
############################################################################

clients = []

def main():
    telegram_thread = threading.Thread(target=Bot_telegram)
    telegram_thread.start()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((SERVER, PORT))
        server.listen(10)
        print("Recebendo conexões em: ", (SERVER, PORT))
    except:
        return print('\nNão foi possível iniciar o servidor!\n')

    while True:
        client, addr = server.accept()
        print(f"\nConexão de: {addr}\n")
        clients.append(client)

        # Inicia uma thread para interação com o cliente
        thread = threading.Thread(target=interacao_Cliente, args=[client, addr])
        thread.start()

def interacao_Cliente(client, addr):
    while True:
        try:
            msg = client.recv(1024)
            informacoes(msg, client, addr)
        except:
            print(f"\nUsuário {addr} desconectado.\n")
            excluir_Cliente(client)
            break

def informacoes(msg, client, addr):
    msg = f"{addr}: {msg.decode('utf-8')}"
    print(msg)
    for clientItem in clients:
        if clientItem != client:
            try:
                clientItem.send(msg.encode('utf-8'))
            except:
                excluir_Cliente(clientItem)

def excluir_Cliente(client):
    clients.remove(client)

def Bot_telegram():
    token = "7216647399:AAEF9mZLGifbRIq3vRE08FUK-L2em_bI8y4"
    strURL = f"https://api.telegram.org/bot{token}/"
    update_id = None
    arquivo_registros = "registros.json"
    registros = function.carregar_registros(arquivo_registros)

    while True:
        try:
            atualizacao = function.obter_atualizacao(update_id, strURL)
            mensagens = atualizacao["result"]
            for mensagem in mensagens:
                update_id = mensagem['update_id']
                chat_id = mensagem['message']['from']['id']
                try:comando = mensagem['message']['text']
                except:comando = "..."
                resposta = function.criar_resposta(comando, chat_id, registros)
                link_de_envio = f"{strURL}sendMessage?chat_id={chat_id}&text={resposta}"
                requests.get(link_de_envio)
        except OSError:
            print("Ocorreu um erro... ", OSError)
        function.guardar_registros(registros, arquivo_registros)

main()
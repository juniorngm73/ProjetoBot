import function

update_id = None

# Token do Bot
token = ''

# URL de acesso ao Bot
strUrl = f'https://api.telegram.org/bot{token}'


while True:
    atualizacao = function.recv_mensagens(update_id, strUrl)
    mensagens = atualizacao
    if mensagens:
        for mensagem in mensagens:
            update_id = mensagem.get('update_id', update_id)
            chat_id = mensagem['message']['from']['id']
            resposta = function.verificar(mensagem, chat_id, strUrl)
            function.respondendo(resposta, chat_id, strUrl)



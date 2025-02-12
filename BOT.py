import json
import sys, requests

# Token do Bot
token = '7216647399:AAEM_FjApKWcjrQb_7Mwg_gp5Eo1Q5dvWeI'

# URL de acesso ao Bot
strUrl = f'https://api.telegram.org/bot{token}'

# Requisição para obter as Mensagens
requisition = requests.get(strUrl + '/getUpdates')

# Verifica se a requisição teve Sucesso
if requisition.status_code != 200:
    sys.exit('\nERRO: Erro na requisição....\n')

# Coverte a resposta da requisição no formato JSON (Dicionário)
json_retorno = requisition.json()

# Exibe o retorno da Requisição
print(f'\n{json_retorno}')

# Obtem o ID do Chat
intIDchat = json_retorno['result'][0]['message']['chat']['id']

# Solicita ao Usuário que digite uma mensagem
mensagem = input('Digite a mensagem a ser enviada: ')

# Dados a serem enviados para o BOT
dictDados = {'chat_id' : intIDchat, 'text':mensagem}

# Envia Mensagem para o BOT
postrequisition = requests.post(strUrl + '/sendmessage', data = dictDados)


import requests, json, os


def carregar_registros(arquivo_registros):
    try:
        arquivo = open(arquivo_registros, "r")
        registros = json.load(arquivo)
        arquivo.close()
        return registros
    except FileNotFoundError:
        return {}


def guardar_registros(registros, arquivo_registros):
    try:
        arquivo = open(arquivo_registros, "w")
        json.dump(registros, arquivo)
        arquivo.close()
    except OSError:
        print(f"Erro ao salvar registros: ", OSError)


def obter_atualizacao(update_id, strURL):
    link_requisicao = f"{strURL}getUpdates?timeout=100"
    if update_id:
        link_requisicao = f"{link_requisicao}&offset={update_id + 1}"
    resultado = requests.get(link_requisicao)
    return json.loads(resultado.content)


def criar_resposta(comando, chat_id, registros):
    dictopcoes = {
        '#INIT': contato_inicial(chat_id, registros), '#HOSTS': informacoes_hosts(), '#SISTEM': informacoes_hardware(),
        '#PROGR': lista_programas_instalados(), '#LOGIN': informacoes_usuario_logado(),
        '#NAVEG': historico_navegacao(), '#ONLINE': lista_agentes_online()
                }

    try:
        return dictopcoes[comando]
    except:
        return mensagem_inicial



def informacoes_hosts():
    return " Situação On line, hostname, IP e Usuario logado"


def informacoes_hardware():
    return "Informações do hardware onde o servidor está sendo executado."


def lista_programas_instalados():
    return "Lista de programas instalados no servidor."


def historico_navegacao():
    return "Histórico de navegação em diferentes navegadores."


def informacoes_usuario_logado():
    return "Informações detalhadas do usuário logado."


def lista_agentes_online():
    return "Lista dos agentes online com informações básicas."




def contato_inicial(chat_id, registros):
    if chat_id not in registros:
        registros[chat_id] = {"primeiro_login": True}
        mensagem_inicio = (
            "Bem-vindo ao Juniorngm_Bot! Nosso contato inicial.\n\n"
            'Para acessar os comandos disponíveis, use o comando "#INIT".'
                          )
        return mensagem_inicio
    else:
        return mensagem_inicial


mensagem_inicial = (
            'Bem Vindo ao Juniorngm_Bot.\n\n'
            'Comandos disponíveis:\n\n'
            'HOSTS --> Situação on line, hostname, IP e Usuário logado.\n'
            '#HOST:IP --> Situação on line, hostname, IP e Usuário logado, correspondente ao IP.\n'
            '#SISTEM --> Informações de Hardware: CPU, Memória,Disco,Sistema Operacional.\n'
            '#SISTEM:IP --> Informações de Hardware: CPU, Memória,Disco,Sistema Operacional,correspondente ao IP.\n'
            '#PROGR --> listagem dos programas instalados.\n' 
            '#PROGR:IP --> listagem dos programas instalados,correspondente ao IP.\n' 
            '#NAVEG --> Histórico de navegação nos navegadores Chrome, Firefox, Microsoft Edge, Opera e Safari.\n'
            '#NAVEG:IP --> Histórico de navegação nos navegadores Chrome, Firefox,  Microsoft Edge, Opera e Safari, correspondente ao IP.\n'
            '#LOGIN --> lista (Home, UID, GID e Shell Padrão).\n'
            '#LOGIN:IP --> lista (Home, UID, GID e Shell Padrão), correspondente ao IP.\n'
            '#ONLINE --> Lista agentes on line (IP, nome do HOST, usuário logado e o tempo que o agente está on-line)\n')

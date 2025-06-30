eventos = []
inscricoes = {}

def cadastrar_evento():
    nome = input("Nome do evento: ")
    data = input("Data do evento (dd/mm/aaaa): ")
    descricao = input("Descrição: ")
    vagas = int(input("Número máximo de participantes: "))
    evento = {"nome": nome, "data": data, "descricao": descricao, "vagas": vagas, "inscritos": 0}
    eventos.append(evento)
    print("Evento cadastrado com sucesso!\n")

def listar_eventos():
    print("\n--- Eventos Disponíveis ---")
    for idx, e in enumerate(eventos):
        vagas_restantes = e["vagas"] - e["inscritos"]
        print(f"{idx+1}. {e['nome']} - {e['data']} | {vagas_restantes} vagas restantes")
        print(f"   Descrição: {e['descricao']}\n")

def inscrever_em_evento():
    listar_eventos()
    escolha = int(input("Digite o número do evento para se inscrever: ")) - 1
    if 0 <= escolha < len(eventos):
        evento = eventos[escolha]
        if evento["inscritos"] < evento["vagas"]:
            nome = input("Seu nome: ")
            inscricoes.setdefault(evento["nome"], []).append(nome)
            evento["inscritos"] += 1
            print("Inscrição realizada com sucesso!\n")
        else:
            print("Evento lotado.\n")
    else:
        print("Evento inválido.\n")

def atualizar_evento():
    listar_eventos()
    idx = int(input("Número do evento a atualizar: ")) - 1
    if 0 <= idx < len(eventos):
        novo_valor = input("Nova data (deixe em branco para manter a atual): ")
        if novo_valor:
            eventos[idx]["data"] = novo_valor
        vagas = input("Novo número de vagas (deixe em branco para manter o atual): ")
        if vagas:
            eventos[idx]["vagas"] = int(vagas)
        print("Evento atualizado!\n")
    else:
        print("Evento inválido.\n")

def excluir_evento():
    listar_eventos()
    idx = int(input("Número do evento a excluir: ")) - 1
    if 0 <= idx < len(eventos):
        nome = eventos[idx]["nome"]
        eventos.pop(idx)
        inscricoes.pop(nome, None)
        print("Evento excluído com sucesso.\n")
    else:
        print("Evento inválido.\n")

def listar_inscritos():
    for nome_evento, lista in inscricoes.items():
        print(f"\nEvento: {nome_evento}")
        for participante in lista:
            print(f" - {participante}")

def menu():
    while True:
        print("""
    === Sistema de Gerenciamento de Eventos - UniFECAF ===
    1. Cadastrar Evento
    2. Listar Eventos
    3. Inscrever-se em Evento
    4. Atualizar Evento
    5. Excluir Evento
    6. Ver Inscrições
    0. Sair
        """)
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_evento()
        elif opcao == "2":
            listar_eventos()
        elif opcao == "3":
            inscrever_em_evento()
        elif opcao == "4":
            atualizar_evento()
        elif opcao == "5":
            excluir_evento()
        elif opcao == "6":
            listar_inscritos()
        elif opcao == "0":
            print("Sistema encerrado. Até a próxima!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Executa o sistema
menu()
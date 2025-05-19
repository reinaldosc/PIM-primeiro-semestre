import json
import os
import time
import hashlib

# Função para criptografar a senha
def gerar_hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

# Função para carregar dados do JSON referente aos usuários
def carregar_usuarios():
    try:
        with open('usuarios.json', 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Função para salvar os usuários
def salvar_usuarios(usuarios):
    with open('usuarios.json', 'w', encoding='utf-8') as arquivo:
        json.dump(usuarios, arquivo, indent=4)

# Cadastro de Usuário
def registrar_usuario():
    limpar_tela()
    usuarios = carregar_usuarios()
    print("---------- Cadastro de Novo Usuário ----------")
    while True:
        usuario = input("Digite um nome de usuário: ")
        if usuario in usuarios:
            print("Usuário já existe! Tente outro.")
        else:
            break
    senha = input("Digite uma senha: ")
    senha_hash = gerar_hash_senha(senha)
    usuarios[usuario] = senha_hash
    salvar_usuarios(usuarios)
    print("Usuário registrado com sucesso!")
    time.sleep(2)

# Login de Usuário
def login_usuario():
    usuarios = carregar_usuarios()
    limpar_tela()
    print("---------- Login ----------")
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    senha_hash = gerar_hash_senha(senha)

    if usuarios.get(usuario) == senha_hash:
        print("Login bem-sucedido!")
        time.sleep(1.5)
        return True
    else:
        print("Usuário ou senha incorretos!")
        time.sleep(2)
        return False

# Função para limpar a tela
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

# Função para carregar dados do JSON referente aos módulos
def carregar_dados():
    try:
        with open('modulos.json', 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo).get("modulos", [])
    except (FileNotFoundError, json.JSONDecodeError):
        print("Erro ao carregar o arquivo 'modulos.json'.")
        exit()

modulos = carregar_dados()

# Exibe o menu inicial
def exibir_menu():
    print(f"{'-'*10} Menu Inicial | Escolha a opção desejada {'-'*10}")
    for i, modulo in enumerate(modulos, start=1):
        print(f"{i} - {modulo['titulo']}")
    print(f"{len(modulos)+1} - Conheça os conteúdos")
    print(f"{len(modulos)+2} - Sair")

# Exibe todos os conteúdos das aulas
def exibir_conteudos():
    for modulo in modulos:
        print(f"\n{modulo['titulo']}")
        for aula in modulo['aulas']:
            print(f" - {aula['titulo']}")
    input("\nAperte ENTER para voltar ao menu...")

# Exibe o conteúdo de uma aula específica
def mostrar_aula(modulo, indice_aula):
    try:
        aula = modulo['aulas'][indice_aula - 1]
        print(f"\n{'-' * 15} {aula['titulo']} {'-' * 15}")
        print(aula['resumo'])
        print(f"\nAssista à aula clicando no link: {aula['link']}")
    except IndexError:
        print("Aula não encontrada.")
    input("\nAperte ENTER para voltar ao módulo...")

# Exibe o módulo escolhido pelo usuário
def acessar_modulo(indice_modulo):
    modulo = modulos[indice_modulo - 1]
    while True:
        limpar_tela()
        print(f"{'-'*10} {modulo['titulo']} {'-'*10}")
        for i, aula in enumerate(modulo['aulas'], start=1):
            print(f"{i} - Assistir aula: {aula['titulo']}")
        print(f"{len(modulo['aulas']) + 1} - Questionário")
        print(f"{len(modulo['aulas']) + 2} - Voltar ao menu")
        try:
            escolha = int(input("Digite o número da opção desejada: "))
        except ValueError:
            print("Entrada inválida!")
            time.sleep(2)
            continue

        if 1 <= escolha <= len(modulo['aulas']):
            limpar_tela()
            mostrar_aula(modulo, escolha)
        elif escolha == len(modulo['aulas']) + 1:
            limpar_tela()
            realizar_questionario(modulo)
            input("\nAperte ENTER para voltar ao módulo...")
        elif escolha == len(modulo['aulas']) + 2:
            break
        else:
            print("Opção inválida!")
            time.sleep(2)

# Exibe o questionário
def realizar_questionario(modulo):
    pontuacao = 0
    for questao in modulo['questionario']:
        for questoes in questao['questoes']:
            print(questoes)
        while True:
            resposta_usuario = input("\nDigite a letra da sua resposta (A, B, C ou D): ").upper()
            if resposta_usuario in ['A', 'B', 'C', 'D']:
                break
            else:
                print("Resposta inválida! Digite A, B, C ou D.")
        if resposta_usuario == questao['resposta_correta']:
            pontuacao += 1
        limpar_tela()

    total_questoes = len(modulo['questionario'])
    print(f"\nVocê acertou {pontuacao} de {total_questoes} questões.")
    porcentagem = (pontuacao / total_questoes) * 100
    print(f"Sua pontuação final foi: {porcentagem:.2f}%")

# Exibe o menu de login
def menu_login():
    while True:
        limpar_tela()
        print("---------- Sistema de Acesso ----------" \
        "\n1 - Login" \
        "\n2 - Registrar novo usuário" \
        "\n3 - Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            if login_usuario():
                return
        elif escolha == "2":
            registrar_usuario()
        elif escolha == "3":
            print("Saindo...")
            exit()
        else:
            print("Opção inválida.")
            time.sleep(2)

# Função principal
def main():
    menu_login()
    while True:
        limpar_tela()
        try:
            exibir_menu()
            opcao = int(input("\nDigite a opção desejada: "))
        except ValueError:
            print("Entrada inválida!")
            time.sleep(2)
            continue
        if 1 <= opcao <= len(modulos):
            acessar_modulo(opcao)
        elif opcao == len(modulos) + 1:
            limpar_tela()
            exibir_conteudos()
        elif opcao == len(modulos) + 2:
            print("\nEncerrando o programa. Até mais!")
            break
        else:
            print("Opção inválida!")
            time.sleep(2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nEncerrando o programa. Até mais!")

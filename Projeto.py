import os
from time import sleep, strftime, localtime
import datetime
from colorama import Fore, Back


def clear():
    os.system("cls")


topicos = ["Livros",
           "Usuários",
           "Empréstimos",
           "Multas e Devoluções",
           "Relátorios",
           "Sair"]

topico_livros = ["Lista de Livros",
                 "Cadastrar Livro",
                 "Buscar livro por título",
                 "Atualizar informações",
                 "Remover livro",
                 "Voltar"]

topico_usuarios = ["Lista de Usuários",
                   "Cadastrar Usuário",
                   "Buscar usuário por nome",
                   "Atualizar cadastro",
                   "Remover Usuário",
                   "Voltar"]

topico_emprestimos = ["Realizar empréstimos",
                      "Realizar devolução",
                      "Verificar disponibilidade",
                      "Ver empréstimo ativos",
                      "Histórico de empréstimos",
                      "Voltar"]

topico_multas = ["Multas pendentes",
                 "Ver lista de inadimplentes",
                 "Voltar"]

topico_relatorios = ["Livros mais emprestados",
                     "Usuários com mais empréstimos",
                     "Estoque atual",
                     "Voltar"]


def retornando():
    print("Retornando...")
    sleep(2)


def enter_to_return():
    input("Pressione ENTER para voltar")

# =========================== Progamação Usuários===================================

# lista_livros = []


class Usuario:
    def __init__(self, nome, livro_emprestimo=None, emprestimos=0):
        self.nome = nome
        self.emprestimos = emprestimos
        self.livro_emprestimo = None
        self.data_emprestimo = None
        self.data_devolucao = datetime.date.today()
        self.data_devolucao_prevista = None
        self.multa = None

    def atualizar(self, nome, livro=None):
        if nome:
            self.nome = nome
            print("User atualizado!")

        if self.livro_emprestimo:
            self.livro_emprestimo = livro
            print('Livro adicionado!')


user1 = Usuario('Iury')
user2 = Usuario('Richard')
user3 = Usuario("Elder")
user4 = Usuario("Daniel")
user5 = Usuario("Marcelo")
user6 = Usuario("Bruno")
lista_usuarios = [user1, user2, user3, user4, user5]


def check_user(nome):
    for usuario in lista_usuarios:
        if nome.lower() == usuario.nome.lower():
            print(f"{nome} está cadastrado")
            return True

    print(f"{nome} não está cadastrado.")


def pull_user(nome):
    for usuario in lista_usuarios:
        if nome.lower() == usuario.nome.lower():
            return usuario
    print("Usuário não encontrado")
    retornando()
    return None


def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")

    novo_usuario = Usuario(nome)
    lista_usuarios.append(novo_usuario)
    print("Usuário cadastrado!!")


def menu_lista_usuarios():
    clear()
    print("====== Lista de Usuários ======")
    for i, usuario in enumerate(lista_usuarios):
        print(f"{i+1} - {usuario.nome}")

    input("Press ENTER to go back ")
    retornando()
    menu_usuarios()


def menu_cadastro_usuarios():
    clear()
    print("===== Cadastro de Usuário =====")
    cadastrar_usuario()
    retornando()
    menu_usuarios()


def menu_buscar_usuarios():
    clear()
    print("===== Buscar Usuário =====")
    nome = input("Digite o usuário: ")
    if (check_user(nome)):
        retornando()
        menu_usuarios()


def menu_atualizar_usuarios():
    clear()
    print("===== Atualizar Nome =====")
    user_atual = input("Digite o usuário atual: ")

    user_atual = pull_user(user_atual)

    novo_user = input("Digite o novo usuario: ")
    user_atual.atualizar(novo_user)
    retornando()
    menu_usuarios()


def menu_remover_usuarios():
    clear()
    print("===== Remover Usuário =====")
    user_encontrado = False
    user_to_remove = input("Digite o usuário: ")

    for user in lista_usuarios:
        if user_to_remove == user.nome:
            lista_usuarios.remove(user)
            print("Usuário removido")
            user_encontrado = True

    if not user_encontrado:
        print("Usuário não encontrado.")

    retornando()
    menu_usuarios()
# =============================== Programação Livro ================================================


class Livro:
    def __init__(self, titulo, emprestimos=0):
        self.titulo = titulo
        self.em_estoque = 'Em estoque'
        self.emprestimos = emprestimos

    def atualizar(self, titulo, estoque):
        if titulo:
            self.titulo = titulo
            print("Livro atualizado!")

        if self.em_estoque:
            self.em_estoque = 'Em estoque' if estoque == 's' else 'Sem estoque'


book1 = Livro("Anatomia")
book2 = Livro("Logica de Programação")
book3 = Livro("Pascal")
book4 = Livro("Álgebra")
lista_livros = [book1, book2, book3, book4]


def check_book(titulo):
    for livro in lista_livros:
        if titulo.lower() == livro.titulo.lower():
            print(f"{titulo} está cadastrado")
            return True

    print(f"{titulo} não está cadastrado.")


def pull_book(titulo):
    for livro in lista_livros:
        if titulo.lower() == livro.titulo.lower():
            return livro
    print("Livro não encontrado")
    retornando()
    return None


def cadastrar_livro():
    titulo = input("Digite o titulo do livro: ")

    novo_livro = Livro(titulo)
    lista_livros.append(novo_livro)
    print("Livro cadastrado!")


def lista_books():
    for i, livro in enumerate(lista_livros):
        print(f"{i+1} - {livro.titulo} ({livro.em_estoque})")
# =======================================================================


def menu_lista_livros():
    clear()
    print("====== Lista de Livros ======")
    lista_books()
    input("Press ENTER to go back ")
    retornando()
    menu_livros()


def menu_cadastrar_livro():
    clear()
    print("===== Cadastro de Livro =====")
    cadastrar_livro()
    retornando()
    menu_livros()


def menu_busca_livro():
    clear()
    print("===== Buscar Livro =====")
    nome = input("Digite o título do livro: ")
    if (check_book(nome)):
        retornando()
        menu_livros()


def menu_atualizar_livro():
    clear()
    print("===== Atualizar Livro =====")
    livro_atual = input("Digite o titulo do livro: ")
    em_estoque = input('Em estoque? [S]im ou [N]ão: ')
    livro_atual = pull_book(livro_atual)

    novo_titulo = input(
        'Digite um novo titulo (Deixe vazio caso não queira mudar...): ')
    livro_atual.atualizar(novo_titulo, em_estoque.lower())

    retornando()
    menu_livros()


def menu_remover_livro():
    clear()
    print("===== Remover Livro =====")
    livro_encontrado = False
    livro_to_remove = input("Digite o título do livro: ")

    for livro in lista_livros:
        if livro_to_remove == livro.titulo:
            lista_livros.remove(livro)
            print("Livro removido")
            livro_encontrado = True

    if not livro_encontrado:
        print("Livro não encontrado.")

    retornando()
    menu_livros()

# ====================== Empréstimos ===============


def realizar_emprestimo(usuario, livro):
    user = pull_user(usuario)
    book = pull_book(livro)

    if not user:
        print("Usuário não encontrado.")
        retornando()
        return

    if not book:
        print("Livro não encontrado.")
        retornando()
        return

    if book.em_estoque != 'Em estoque':
        print("Livro indisponível para empréstimo.")
        return

    user.livro_emprestimo = livro
    user.data_emprestimo = datetime.date.today()
    user.data_devolucao_prevista = user.data_emprestimo + \
        datetime.timedelta(days=7)
    user.emprestimos += 1
    book.emprestimos += 1
    book.em_estoque = 'Sem estoque'
    print("===============================================")
    print(f"Empréstimo realizado com sucesso para {user.nome}")
    print(f'{user.nome} tem 7 dias para devolução.')
    print(f"{Back.LIGHTRED_EX}Obs* caso devolva após 7 dias, será aplicada\n"
          f"uma multa de R$1,00 por dia útil{Back.RESET}")
    enter_to_return()
    retornando()
    menu_emprestimos()


def verificar_disponibilidade(livro):
    book_exists = False
    for book in lista_livros:
        if livro.lower() == book.em_estoque.lower():
            if book.em_estoque == 'Em estoque':
                book_exists = True

    if not book_exists:
        print('Livro não disponível para empréstimo.')
    else:
        print('Livro disponível para empréstimo.')


def emprestimos_ativos():
    livros_emprestados = 0
    print(f'{"USUÁRIO":<10} {"LIVRO":<10} {"DATA PREVISTA":>10}')
    for user in lista_usuarios:
        if user.livro_emprestimo is not None:
            print(
                f'{user.nome:<10} {user.livro_emprestimo:<10} \t {user.data_devolucao_prevista.strftime('%d/%m/%Y'):<10}')

            livros_emprestados += 1

    if livros_emprestados == 0:
        print('Nenhum livro foi emprestado...')

    enter_to_return()
    retornando()
    menu_emprestimos()


def historico_emprestimo():
    print(f'{"DATA":<10} {"LIVRO":<10} {"USUÁRIO":<10}')
    for user in lista_usuarios:
        if user.livro_emprestimo is not None:
            print(
            f'{user.data_emprestimo.strftime("%d/%m/%Y"):<10} {user.livro_emprestimo:<10} {user.nome:<10}')
                

def menu_realizar_emprestimo():
    clear()
    print("===== Realizar Emprestimos =====")
    lista_books()
    print("5 - Voltar")
    usuario_atual = input("Digite o usuário: ")
    while True:
        livro_indice = input("Digite o índice do livro que desejas: ")
        if livro_indice.isdigit():
            livro_indice = int(livro_indice)
            if livro_indice == 5:
                retornando()
                menu_emprestimos()
            break
        else:
            print("Entrada Inválida!")
    usuario_atual = pull_user(usuario_atual)
    for user in lista_usuarios:
        if usuario_atual.livro_emprestimo is None:
            livro = lista_livros[livro_indice - 1]

            realizar_emprestimo(usuario_atual.nome, livro.titulo)
            break
        else:
            print('Este usuário já possui um empréstimo...')
            break
    retornando()
    menu_emprestimos()


def menu_realizar_devolucao():
    clear()
    print("===== Realizar Devolução ======")
    usuario_atual = input("Digite o usuario: ")
    usuario_atual = pull_user(usuario_atual)

    print(f"{usuario_atual.nome} devolveu {usuario_atual.livro_emprestimo}")
    data = input("Digite a data de devolução (dd/mm/aa): ")
    usuario_atual.data_devolucao = datetime.datetime.strptime(data, "%d/%m/%Y")

    livro = pull_book(usuario_atual.livro_emprestimo)
    livro.em_estoque = "Em estoque"
    usuario_atual.livro_emprestimo = None
    print(calcular_multa(usuario_atual))

    enter_to_return()
    retornando()
    menu_emprestimos()


def menu_verificar_disponibilidade():
    clear()
    print("===== Verificar Disponibilidade =====")
    lista_books()
    retornando()
    menu_emprestimos()


def menu_emprestimos_ativos():
    clear()
    print("===== Empréstimos Ativos =====")
    emprestimos_ativos()
    retornando()
    menu_emprestimos()


def menu_historico_emprestimo():
    clear()
    print("===== Histórico de Empréstimo =====")
    historico_emprestimo()
    enter_to_return()
    menu_emprestimos()
# ====================== Progaramação Multas ===============


def calcular_multa(usuario):
    hoje = datetime.date.today()
    dias_atraso = (usuario.data_devolucao.date() - hoje).days

    if dias_atraso > 7:
        valor_multa = (dias_atraso - 7) * 1.00
        usuario.multa = f"{usuario.nome} está com R${valor_multa:.2f} em multas"
    else:
        if usuario.data_devolucao.date() > hoje:
            usuario.multa = f"O usuário {usuario.nome} está em dias..."
        else:
            print("Data inválida...")
    return usuario.multa


def lista_inadimplentes():
    print(f'{"USUÁRIO":<10} {"STATUS":<20}')
    print("=========================================")
    for user in lista_usuarios:
        if user.multa is not None:
            print(f'{user.nome:<10} {user.multa:<20}')
            print("=========================================")


def menu_multas_pendentes():
    clear()
    print("===== Multas Pendentes =====")
    usuario_atual = input("Digite o usuário: ")
    usuario_atual = pull_user(usuario_atual)
    print(calcular_multa(usuario_atual))
    enter_to_return()
    retornando()
    menu_multas()


def menu_inadimplentes():
    clear()
    print("===== Lista de Inadimplentes =====")
    lista_inadimplentes()
    enter_to_return()
    retornando()
    menu_emprestimos()


# ================================ Relatórios =========================================================


def livros_mais_emprestados():

    livros_ordenados = sorted(
        lista_livros, key=lambda livro: livro.emprestimos, reverse=True)
    return livros_ordenados


def usuarios_com_mais_emprestimos():

    usuarios_ranking = []

    for user in lista_usuarios:
        usuarios_ranking.append(
            {"nome": user.nome, "pontos": user.emprestimos})

    usuarios_ranking.sort(key=lambda x: x["pontos"], reverse=True)

    return usuarios_ranking


def menu_livros_mais_emprestados():
    clear()
    print("===== Livros Mais Emprestados ======")

    for i, livro in enumerate(livros_mais_emprestados()):
        print(f"{i+1}° {livro.titulo} - {livro.emprestimos} empréstimos")
    enter_to_return()
    menu_relatorios()


def menu_usuarios_com_mais_emprestimos():
    clear()
    print("===== Usuários Com Mais Empréstimos ======")
    for i, usuario in enumerate(usuarios_com_mais_emprestimos()):
        print(f"{i+1}° {usuario['nome']} - {usuario['pontos']} empréstimos")
    enter_to_return()
    menu_relatorios()


def menu_estoque_atual():
    clear()
    print("===== Estoque =====")
    lista_books()
    enter_to_return()
    menu_relatorios()

# =============================== Menu principal ================================================


def menu_principal():

    clear()
    print("===== Menu Principal =====")
    for i in range(len(topicos)):
        print(f"{i + 1} - {topicos[i]}")

    option = int(input("Digite a opção desejada: "))

    if option == 1:
        menu_livros()

    elif option == 2:
        menu_usuarios()

    elif option == 3:
        menu_emprestimos()

    elif option == 4:
        menu_multas()

    elif option == 5:
        menu_relatorios()

    elif option == 6:
        print("Saindo...")
        sleep(2)
        clear()

    else:
        print("❌Opção Inválida")


def choose_option():
    option = int(input("Digite a opção desejada: "))
    return option
# =========================== Menu Livros ===================================


def menu_livros():
    clear()
    print("===== Livros =====")
    for i in range(len(topico_livros)):
        print(f'{i + 1} - {topico_livros[i]}')

    escolha = choose_option()
    if escolha == 1:
        menu_lista_livros()

    elif escolha == 2:
        menu_cadastrar_livro()

    elif escolha == 3:
        menu_busca_livro()

    elif escolha == 4:
        menu_atualizar_livro()

    elif escolha == 5:
        menu_remover_livro()

    elif escolha == 6:
        menu_principal()

    else:
        print("❌Valor inválido, digite novamente")
        retornando()
        menu_livros()
# =========================== Menu Usuarios ===================================


def menu_usuarios():
    clear()
    print("===== Usuários =====")
    for i in range(len(topico_usuarios)):
        print(f'{i + 1} - {topico_usuarios[i]}')

    escolha = choose_option()
    if escolha == 1:
        menu_lista_usuarios()

    elif escolha == 2:
        menu_cadastro_usuarios()

    elif escolha == 3:
        menu_buscar_usuarios()

    elif escolha == 4:
        menu_atualizar_usuarios()

    elif escolha == 5:
        menu_remover_usuarios()

    elif escolha == 6:
        menu_principal()
    else:
        print("❌Valor inválido, digite novamente")
        retornando()
        menu_livros()
# =========================== Menu Empréstimos ===================================


def menu_emprestimos():
    clear()
    print("===== Empréstimos =====")
    for i in range(len(topico_emprestimos)):
        print(f'{i + 1} - {topico_emprestimos[i]}')

    escolha = choose_option()
    if escolha == 1:
        menu_realizar_emprestimo()

    elif escolha == 2:
        menu_realizar_devolucao()

    elif escolha == 3:
        menu_verificar_disponibilidade()

    elif escolha == 4:
        menu_emprestimos_ativos()

    elif escolha == 5:
        menu_historico_emprestimo()

    elif escolha == 6:
        menu_principal()

    else:
        print("❌Valor inválido, digite novamente")
        retornando()
        menu_livros()
# =========================== Menu Multas ===================================


def menu_multas():
    clear()
    print("===== Multas =====")
    for i in range(len(topico_multas)):
        print(f'{i + 1} - {topico_multas[i]}')

    escolha = choose_option()

    if escolha == 1:
        menu_multas_pendentes()

    elif escolha == 2:
        menu_inadimplentes()
    elif escolha == 3:
        menu_principal()
    else:
        print("❌Valor inválido, digite novamente")
        retornando()
        menu_livros()

# =========================== Menu Relatorios ===================================


def menu_relatorios():
    clear()
    print("===== Relatórios =====")
    for i in range(len(topico_relatorios)):
        print(f'{i + 1} - {topico_relatorios[i]}')

    escolha = choose_option()

    if escolha == 1:
        menu_livros_mais_emprestados()
    elif escolha == 2:
        menu_usuarios_com_mais_emprestimos()
    elif escolha == 3:
        menu_estoque_atual()
    elif escolha == 4:
        menu_principal()
    else:
        print("❌Valor inválido, digite novamente")
        retornando()
        menu_livros()


# =========================== Main function ===================================
while True:
    clear()
    menu_principal()
    break

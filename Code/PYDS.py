class Livro:
    def __init__(self, titulo, autor, copias):
        self.titulo, self.autor, self.copias = titulo, autor, copias

biblioteca, emprestimos = [], {}

while True:
    print("\n1. Adicionar Livro\n2. Listar Livros\n3. Emprestar Livro\n4. Devolver Livro\n5. Verificar Disponibilidade\n6. Mostrar Livros Emprestados\n7. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        titulo, autor, copias = input("Título: "), input("Autor: "), int(input("Cópias: "))
        biblioteca.append(Livro(titulo, autor, copias))
        print(f'Livro "{titulo}" adicionado!')

    elif opcao == '2':
        if not biblioteca:
            print("Nenhum livro disponível.")
        else:
            for livro in biblioteca:
                print(f'Título: {livro.titulo}, Autor: {livro.autor}, Cópias: {livro.copias}')

    elif opcao == '3':
        titulo, usuario = input("Título: "), input("Usuário: ")
        livro = next((l for l in biblioteca if l.titulo == titulo), None)
        if livro and livro.copias > 0:
            livro.copias -= 1
            emprestimos.setdefault(usuario, []).append(titulo)
            print(f'Livro "{titulo}" emprestado a {usuario}.')
        else:
            print(f'Livro "{titulo}" indisponível.' if livro else f'Livro não encontrado.')

    elif opcao == '4':
        titulo, usuario = input("Título: "), input("Usuário: ")
        if usuario in emprestimos and titulo in emprestimos[usuario]:
            livro = next((l for l in biblioteca if l.titulo == titulo), None)
            livro.copias += 1
            emprestimos[usuario].remove(titulo)
            if not emprestimos[usuario]: del emprestimos[usuario]
            print(f'Livro "{titulo}" devolvido por {usuario}.')
        else:
            print(f'Usuário não possui o livro.')

    elif opcao == '5':
        titulo = input("Título: ")
        livro = next((l for l in biblioteca if l.titulo == titulo), None)
        print(f'Cópias disponíveis: {livro.copias}' if livro else 'Livro não encontrado.')

    elif opcao == '6':
        usuario = input("Usuário: ")
        print(f'Livros de {usuario}: {", ".join(emprestimos[usuario])}' if usuario in emprestimos else 'Nenhum livro emprestado.')

    elif opcao == '7':
        break

    else:
        print("Opção inválida.")

#Um Professor me fez estudar muito e consegui resumir minhas 120 linhas em 57 ^^ - Dei meu melhor !!        
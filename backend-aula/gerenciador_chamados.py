chamados = [
    {
        "id": 1,
        "titulo": "Sem acesso ao sistema interno",
        "prioridade": "alta",
        "situacao": "aberto",
        "categoria": "acesso"
    },
    {
        "id": 2,
        "titulo": "Impressora sem conexão",
        "prioridade": "média",
        "situacao": "em atendimento",
        "categoria": "hardware"
    },
    {
        "id": 3,
        "titulo": "Senha expirada",
        "prioridade": "alta",
        "situacao": "aberto",
        "categoria": "acesso"
    },
    {
        "id": 4,
        "titulo": "Computador apresentando lentidão",
        "prioridade": "média",
        "situacao": "resolvido",
        "categoria": "hardware"
    },
    {
        "id": 5,
        "titulo": "Erro no sistema de cadastro",
        "prioridade": "baixa",
        "situacao": "aberto",
        "categoria": "software"
    }
]


print("===== LISTA DE TODOS OS CHAMADOS =====")

for chamado in chamados:
    print(f"ID: {chamado['id']}")
    print(f"Título: {chamado['titulo']}")
    print(f"Prioridade: {chamado['prioridade']}")
    print(f"Situação: {chamado['situacao']}")
    print(f"Categoria: {chamado['categoria']}")
    print("-" * 30)


print("\n===== FILTRO POR SITUAÇÃO =====")

situacao_desejada = "aberto"
encontrou_chamado = False

for chamado in chamados:
    if chamado["situacao"] == situacao_desejada:
        print(f"ID: {chamado['id']}")
        print(f"Título: {chamado['titulo']}")
        print(f"Prioridade: {chamado['prioridade']}")
        print(f"Situação: {chamado['situacao']}")
        print(f"Categoria: {chamado['categoria']}")
        print("-" * 30)

        encontrou_chamado = True

if not encontrou_chamado:
    print(
        f"Nenhum chamado encontrado com a situação: "
        f"{situacao_desejada}"
    )


print("\n===== TESTE DE SITUAÇÃO INEXISTENTE =====")

situacao_desejada = "cancelado"
encontrou_chamado = False

for chamado in chamados:
    if chamado["situacao"] == situacao_desejada:
        print(f"ID: {chamado['id']}")
        print(f"Título: {chamado['titulo']}")
        print(f"Prioridade: {chamado['prioridade']}")
        print(f"Situação: {chamado['situacao']}")
        print(f"Categoria: {chamado['categoria']}")
        print("-" * 30)

        encontrou_chamado = True

if not encontrou_chamado:
    print(
        f"Nenhum chamado encontrado com a situação: "
        f"{situacao_desejada}"
    )


print("\n===== ATUALIZAÇÃO DE CHAMADO =====")

id_chamado = 2
nova_situacao = "resolvido"
encontrou_chamado = False

for chamado in chamados:
    if chamado["id"] == id_chamado:
        chamado["situacao"] = nova_situacao

        print(f"Chamado {id_chamado} atualizado com sucesso.")
        print(f"Nova situação: {chamado['situacao']}")

        encontrou_chamado = True
        break

if not encontrou_chamado:
    print("Chamado não encontrado.")


print("\n===== TESTE DE ID INEXISTENTE =====")

id_chamado = 99
nova_situacao = "resolvido"
encontrou_chamado = False

for chamado in chamados:
    if chamado["id"] == id_chamado:
        chamado["situacao"] = nova_situacao

        print(f"Chamado {id_chamado} atualizado com sucesso.")

        encontrou_chamado = True
        break

if not encontrou_chamado:
    print("Chamado não encontrado.")


print("\n===== CATEGORIAS SEM REPETIÇÃO =====")

categorias = set()

for chamado in chamados:
    categorias.add(chamado["categoria"])

print("Categorias encontradas:")

for categoria in categorias:
    print(f"- {categoria}")

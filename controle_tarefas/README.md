# Controle de Tarefas
## Alunos

- João Lucas Binttencourt Rocha - 202422927
- João Pedro Oliveira - 202422911
- José Carlos Silva Pimentel - 202422916
- Adriel dos Santos Azevedo - 202422733

## Objetivo

Refatorar um sistema de controle de tarefas utilizando funções e programação orientada a objetos.

A atividade tem como objetivo separar as responsabilidades do programa em diferentes arquivos, tornando o código mais organizado, reutilizável e fácil de manter.

## Funcionalidades

O sistema demonstra:

- Criação de tarefas;
- Cadastro de tarefas;
- Listagem de tarefas;
- Conclusão de tarefas;
- Filtro de tarefas por situação.

## Organização

tarefa.py: contém a classe Tarefa, seus atributos e métodos.
servicos.py: contém as funções para cadastrar, listar e filtrar tarefas.
main.py: arquivo principal responsável por executar e demonstrar o funcionamento do sistema.

## Funcionalidades

O programa demonstra:

- Cadastro de tarefas;
- Armazenamento das tarefas em uma lista;
- Exibição das tarefas cadastradas;
- Alteração da situação de uma tarefa para "Concluída";
- Filtro de tarefas por situação.

### Exemplo de saída
Todas as tarefas:
1. Título: Revisar chamados | Prioridade: Alta | Situação: Concluída
2. Título: Atualizar manual interno | Prioridade: Média | Situação: Pendente
3. Título: Planejar reunião | Prioridade: Baixa | Situação: Pendente

Tarefas concluídas:
1. Título: Revisar chamados | Prioridade: Alta | Situação: Concluída
# Controle de Tarefas
## Alunos

João Lucas Binttencourt Rocha - 202422927
João Pedro Oliveira - 202422911

## Objetivo

O projeto apresenta uma refatoração de um sistema simples de controle de tarefas, utilizando uma classe para representar as tarefas e funções separadas para realizar as operações do sistema.

A atividade demonstra conceitos de programação orientada a objetos, funções, listas e filtros.

## Execução

Abra o terminal dentro da pasta controle_tarefas e execute:

python main.py


Caso o ambiente utilize python3, execute:

python3 main.py

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
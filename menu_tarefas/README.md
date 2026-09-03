# Menu de Tarefas

## Alunos
- João Lucas Binttencourt Rocha - 202422927
- João Pedro Oliveira - 202422911
- José Carlos Silva Pimentel - 202422916
- Adriel dos Santos Azevedo - 202422733

## Objetivo

Desenvolver um sistema simples de gerenciamento de tarefas utilizando um menu interativo no terminal.

A atividade tem como objetivo praticar estruturas de decisão, estruturas de repetição, listas, dicionários e validação de dados.

## Funcionalidades

O sistema possui quatro opções:

## Cadastrar tarefa

Solicita o título da tarefa.
Solicita a prioridade.
Valida os dados informados.
Cadastra a tarefa com situação inicial pendente.

## Listar tarefas

Exibe todas as tarefas cadastradas.
Mostra número, título, prioridade e situação.
Informa quando não existem tarefas cadastradas.

## Atualizar situação

Solicita o número da tarefa.
Verifica se a entrada contém apenas números.
Altera a situação da tarefa para concluída.
Informa quando a tarefa não existe.

## Encerrar sistema

Encerra o programa.
Conceitos utilizados
while
for
if, elif e else
Listas
Dicionários
input()
Validação de dados
.strip()
.lower()
.isdigit()
Execução

Abra o terminal dentro da pasta da atividade e execute:

python menu_tarefas.py


Caso seja necessário utilizar python3:

python3 menu_tarefas.py

## Exemplo de uso
- 1 - Cadastrar tarefa
- 2 - Listar tarefas
- 3 - Atualizar situação
- 4 - Encerrar sistema

Escolha uma opção: 1

Digite o título da tarefa: Revisar relatório
Digite a prioridade (alta, média ou baixa): alta

Tarefa cadastrada com sucesso.

## Limitações

Os dados das tarefas são armazenados apenas durante a execução do programa.

Ao encerrar o sistema, todas as tarefas cadastradas são perdidas, pois não existe banco de dados ou armazenamento permanente.

## Arquivo principal
menu_tarefas.py — contém o código do sistema de gerenciamento de tarefas.
# Gerenciador de Chamados Internos

## Alunos

- João Lucas Binttencourt Rocha - 202422927
- João Pedro Oliveira - 202422911
- José Carlos Silva Pimentel - 202422916
- Adriel dos Santos Azevedo - 202422733

## Objetivo

Desenvolver um programa para gerenciamento de chamados internos de uma equipe de serviços.

A atividade tem como objetivo praticar listas, dicionários, estruturas de repetição, filtros, atualização de dados e conjuntos (set).

## Funcionalidades

O programa realiza as seguintes operações:

Lista todos os chamados cadastrados;
Filtra chamados por situação;
Informa quando nenhum chamado atende ao filtro;
Atualiza a situação de um chamado pelo ID;
Informa quando um chamado não é encontrado;
Exibe as categorias cadastradas sem repetição.

## Dados dos chamados

Cada chamado possui as seguintes informações:

- id
- titulo
- prioridade
- situacao
- categoria
- O programa possui inicialmente cinco chamados cadastrados.

## Conceitos utilizados
- Listas
- Dicionários
- Estruturas for
- Estruturas if
- Variáveis de controle
- Busca por identificador
- Alteração de dados
- Conjuntos utilizando set()

## Execução

Abra o terminal dentro da pasta da atividade e execute:

python gerenciador_chamados.py

Caso seja necessário utilizar python3:

python3 gerenciador_chamados.py

# Exemplo de saída

===== LISTA DE TODOS OS CHAMADOS =====

ID: 1
Título: Sem acesso ao sistema interno
Prioridade: alta
Situação: aberto
Categoria: acesso
------------------------------

===== ATUALIZAÇÃO DE CHAMADO =====

Chamado 2 atualizado com sucesso.
Nova situação: resolvido

===== CATEGORIAS SEM REPETIÇÃO =====

Categorias encontradas:
- acesso
- hardware
- software

## Limitações

Os chamados são armazenados diretamente no código e ficam disponíveis apenas durante a execução.

As alterações realizadas não são salvas permanentemente após o encerramento do programa.

O programa ainda não utiliza banco de dados ou arquivos para armazenamento permanente.

## Arquivo principal

gerenciador_chamados.py — contém os dados iniciais e as operações do gerenciador de chamados.
# ALUNOS: 
- João Lucas Binttencourt Rocha - 202422927
- João Pedro Oliveira - 202422911
- José Carlos Silva Pimentel - 202422916
- Adriel dos Santos Azevedo - 202422733

# Atividades Back End

Repositório destinado ao armazenamento e organização das atividades práticas desenvolvidas durante as aulas de Laboratório de Desenvolvimento Back-end.

## Sobre o repositório

Este repositório reúne os exercícios e projetos realizados ao longo da disciplina, organizados de forma separada para facilitar a consulta e o acompanhamento das atividades. Cada atividade possui sua própria pasta, contendo seus respectivos arquivos, códigos e documentações.

A proposta é registrar e acompanhar a evolução dos conhecimentos em desenvolvimento back-end, passando pelos conceitos fundamentais até a criação de aplicações mais completas, além de reforçar e revisar os conteúdos trabalhados durante as aulas.

## Pré-requisito

Para executar as atividades, é necessário ter o Python 3 instalado no computador.

## Execução 

Crie o ambiente virtual:

python -m venv .venv
Windows

Ative o ambiente virtual:

.venv\Scripts\activate

Execute o script:

python main.py
Linux / macOS

Ative o ambiente virtual:

source .venv/bin/activate

Execute o script:

python main.py

## Atividade — Menu de tarefas
Nesta atividade foi desenvolvido um sistema simples de gerenciamento de tarefas para uma equipe de serviços.

O programa funciona por meio de um menu interativo no terminal e permite:

Cadastrar uma tarefa;
Listar as tarefas cadastradas;
Atualizar a situação de uma tarefa para concluída;
Encerrar o sistema.
As tarefas são armazenadas temporariamente em uma lista enquanto o programa está em execução.

## Atividade - Gerenciador de chamados
O programa tem como objetivo gerenciar chamados internos de uma equipe de serviços.

A aplicação utiliza uma lista de dicionários para armazenar os chamados e demonstra conceitos básicos de Python, como:

Listas e dicionários;
Estruturas de repetição com for;
Estruturas condicionais com if;
Filtros por situação;
Atualização de dados pelo identificador;
Conjuntos (set) para evitar categorias repetidas.

## Limitações conhecidas
Os dados são armazenados apenas durante a execução do programa.
As tarefas são perdidas quando o sistema é encerrado.
O programa ainda não utiliza banco de dados ou arquivos para armazenamento permanente.
Não é possível excluir tarefas cadastradas.
A opção de atualização altera apenas a situação da tarefa para concluída.

## Organização

As atividades são organizadas da seguinte forma:

```text
Atividades Back Ends/
│
├── Atividade 1/
│   ├── main.py
│   ├── requirements.txt
│   ├── README.md
│   ├── .gitignore
│   ├── cadastro_tarefa.py
│   ├── menu_tarefas.py
│   └── gerenciador_chamados.py
│
└── ...
```

## Estrutura do projeto

- main.py — arquivo principal responsável pela execução do projeto.
- cadastro_tarefa.py — arquivo responsável pelo cadastro e processamento das informações de uma tarefa.
- requirements.txt — arquivo que reúne as dependências necessárias para executar a aplicação.
- .gitignore — arquivo que define quais arquivos e pastas devem ser ignorados pelo Git.

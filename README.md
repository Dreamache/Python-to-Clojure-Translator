# Python-to-Clojure-Translator

# Requisitos do tradutor atirmetico

O código utiliza a biblioteca padrão 'ast' para analisar a sintaxe das expressões lógicas em Python.

Descrição do Sistema:
O código fornece funções para converter expressões matemáticas escritas em Python para a linguagem Clojure. Ele consiste em três principais componentes: lexer, parser e translate.

Requisitos Funcionais:
2.1. Lexer:

O lexer deve receber uma expressão matemática escrita em Python como entrada.
Ele deve dividir a expressão em tokens, identificando números, variáveis e operadores.
Os tokens devem ser retornados na forma de uma lista.
2.2. Parser:

O parser deve receber a lista de tokens gerada pelo lexer como entrada.
Ele deve construir uma árvore de sintaxe abstrata (AST) para representar a expressão matemática.
A AST deve ser retornada na forma de uma estrutura de dados aninhada.
2.3. Translate:

O translate deve receber a AST gerada pelo parser como entrada.
Ele deve percorrer a AST e converter os nós em uma representação de string na linguagem Clojure.
A expressão traduzida em Clojure deve ser retornada como uma string.
2.4. python_to_clojure:

A função python_to_clojure deve receber uma expressão matemática escrita em Python como entrada.
Ela deve chamar as funções lexer, parser e translate, nesta ordem, para realizar a conversão para Clojure.
A expressão traduzida em Clojure deve ser retornada como uma string.
2.5. Main:

O código principal deve conter uma lista de expressões matemáticas escritas em Python.
Para cada expressão, deve-se imprimir a expressão original em Python e sua tradução em Clojure, separadas por uma linha vazia.

# Requisitos do tradutor booleano

Descrição do Sistema:
O código tem como objetivo converter expressões lógicas escritas em Python para a linguagem Clojure. 
Ele utiliza a biblioteca padrão 'ast' do Python para analisar a sintaxe da expressão e construir uma representação equivalente em Clojure.

Requisitos Funcionais:
2.1. translate_expression:

A função translate_expression deve receber um nó da árvore sintática abstrata (AST) do Python como entrada.
Ela deve percorrer a AST e traduzir o nó para a representação equivalente em Clojure.
A expressão traduzida em Clojure deve ser retornada como uma string.
2.2. translate_python_to_clojure:

A função translate_python_to_clojure deve receber uma expressão lógica escrita em Python como entrada.
Ela deve utilizar a função translate_expression para traduzir a expressão para Clojure.
A expressão traduzida em Clojure deve ser retornada como uma string.
2.3. Main:

O código principal deve receber uma expressão lógica escrita em Python como entrada.
Ele deve chamar a função translate_python_to_clojure para realizar a conversão.
A expressão traduzida em Clojure deve ser impressa na tela.

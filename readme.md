Restaurant Analysis and Management System (Infnet Academic Project)

🇺🇸

This project was developed as part of the Python for Data Science discipline at Instituto Infnet.

The objective was to build a complete system for analyzing and managing restaurants, combining data processing using Python and Object-Oriented Programming (OOP) principles.

The work spans from reading and cleaning CSV files to creating classes, exporting data in JSON, implementing validations, generating rankings, and organizing the code modularly.

👾 Core Features

1. Reading and Inspection

Reading the pedidos_e_avaliacoes.csv file;

Displaying:
Number of rows and columns;
Data types per column;
Three random data samples.

2. Data Cleaning
Removal of invalid reviews (outside the 1–5 range or missing values);
Exclusion of records with null or $\le 0$ price;
Standardization of categories to lowercase;
Removal of extra spaces in names;
Counting of removed records.

3. Normalization
Removal of exact duplicates;
Creation of the faixa_preco (price_range) column ("baixo", "médio", "alto");
Creation of the tamanho_nome_item (item_name_length) column (number of characters in the item name).

4. Quick Checks
Counting distinct clients, restaurants, and items;
Groupings by category and price range.

5. System Classes (OOP)
Prato (Dish) and Bebida (Drink): Contain name, price, and ratings.
Restaurante (Restaurant): Groups dishes and drinks, allows for searching, and prevents internal duplication.
Cliente (Client): Manages favorites and prevents duplication or removal errors.

6. Validations and Methods
Prevents duplicate items and invalid names;
Allows listing items by category;
Ensures consistency in favorites lists.

7. Transaction Register to File
Generation of a transaction file (extrato_sj90.txt) containing client transactions;
Reading and displaying the file content in the terminal.

8–9. Client Export and Filtering
Exporting the client database (clientes_sj90.json);
Creation of a new file (clientes_premium.json) with clients having a balance greater than 1000.

10. Rankings
Top 3 restaurants with the highest average rating (tie-breaker: number of reviews);
Top 3 items with the best average rating (tie-breaker: lowest price).

11. Modularization
Code divided into modules to facilitate maintenance and reuse.

💻 Technologies Used

Python 3.11+
Pandas (for data reading and cleaning)
JSON and CSV (for data export)
OOP (Object-Oriented Programming)

💬 Note
This project was developed for academic purposes but follows a professional structure with organized commits and modular code, simulating a real-world data analysis and simple backend project.

🇧🇷

Este projeto foi desenvolvido como parte da disciplina Python para Dados no Instituto Infnet.
O objetivo foi construir um sistema completo de análise e gerenciamento de restaurantes, combinando tratamento de dados com Python e Programação Orientada a Objetos (POO).

O trabalho envolve desde a leitura e limpeza de arquivos CSV até a criação de classes, exportação em JSON, validações, rankings e organização modular do código.

👾 Funcionalidades Principais

1. Leitura e Inspeção

Leitura do arquivo pedidos_e_avaliacoes.csv;

Exibição de:
Quantidade de linhas e colunas;
Tipos de dados por coluna;
Três amostras da base.

2. Limpeza de Dados

Remoção de avaliações inválidas (fora de 1–5 ou ausentes);
Exclusão de registros com preço nulo ou ≤ 0;
Padronização da categoria em minúsculas;
Remoção de espaços extras em nomes;
Contagem de registros removidos.

3. Normalizações

Remoção de duplicatas exatas;
Criação da coluna faixa_preco (“baixo”, “médio”, “alto”);
Criação da coluna tamanho_nome_item (número de caracteres do item).

4. Checagens rápidas

Contagem de clientes, restaurantes e itens distintos;
Agrupamentos por categoria e faixa de preço.

5. Classes do Sistema

Prato e Bebida: possuem nome, preço e notas.
Restaurante: agrupa pratos e bebidas, permite buscas e evita duplicações.
Cliente: gerencia favoritos e evita erros de duplicação ou remoção.

6. Validações e Métodos

Evita itens duplicados e nomes inválidos;
Permite listar itens por categoria;
Garante consistência nas listas de favoritos.

7. Registro de Extratos em Arquivo

Geração de um arquivo extrato_sj90.txt com transações de clientes;
Leitura e exibição do arquivo no terminal.

8–9. Exportação e Filtro de Clientes

Exportação da base de clientes (clientes_sj90.json);
Criação de um novo arquivo clientes_premium.json com clientes saldo > 1000.

10. Rankings

Top 3 restaurantes com maiores médias (desempate: número de avaliações);
Top 3 itens com melhores médias (desempate: menor preço).

11. Modularização

Código dividido em módulos para facilitar manutenção e reuso.


💻 Tecnologias Utilizadas

Python 3.11+
Pandas (para leitura e limpeza de dados)
JSON e CSV (para exportação)
POO (Programação Orientada a Objetos)

💬 Observação

Este projeto foi desenvolvido com fins acadêmicos, mas segue uma estrutura profissional com commits organizados e código modular, simulando um projeto real de análise de dados e backend simples.

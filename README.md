# Modelo de recomendação de imóveis com PySpark

Rápida descrição do objetivo de fazer esse projeto

| :placard: Vitrine.Dev | https://cursos.alura.com.br/vitrinedev/gabrielzuli22
| -------------  | --- |
| :sparkles: Nome        | **Desafio Data Science Alura**
| :label: Tecnologias | Python, PySpark, Aprendizado de Máquina
| :rocket: URL         | https://github.com/kennenvi/Challange-Dados
| :fire: Desafio     | https://www.alura.com.br/challenges/data-science-2?host=https://cursos.alura.com.br

<!-- Inserir imagem com a #vitrinedev ao final do link -->
![](https://via.placeholder.com/1200x500.png?text=imagem+lindona+do+meu+projeto#vitrinedev)

## Detalhes do projeto

Esse projeto foi feito para o Alura Desafio dados, onde foi apresentado um conjunto de dados sobre imóveis que serão
primeiramente, explorados e processados, após isso será construido um modelo de regressão para prever o valor de imóveis baseando-se em suas características
e por último a elaboração de um sistema de recomendação utilizando um algoritmo de clusterização para recomendar imóveis.
No projeto foi utilizada a linguagem Python no ambiente do google Colab em conjunto a ferramenta PySpark para o processamento de grandes quantidades de dados e com o módulo de aprendizado de máquina do próprio PySpark para a criação dos modelo.


### Processamento do Conjunto de dados com PySpark

Nessa etapa foi realizada a exploração do conjunto de dados a fim de extrair informações e 
realizar transformações necessárias para as fases seguintes. Os passos realizados foram:

* Importar dados em formatato JSON
* Selecionar colunas desejadas em meio a colunas e subcolunas
* Atribuir os tipos de dados certos para as colunas
* Salvar os dados no formato parquet

### Criando modelo de regressão para estimar preços de imóveis

Nessa etapa foram construídos diferentes modelos de regressão utilizando 
o módulo de aprendizado de máquina do PySpark. Os passos realizados foram:

* Processar os dados faltandos do conjunto de dados
* Analisar quais as melhores features para inserir no modelo
* Preparar os dados para inserção no modelo, trasnformando-os em vetores
* Criação dos modelos de regressão e avaliando-os com métricas como r2
* Otimização dos hiperparâmetros
* Validação cruzada

### Construindo modelo de recomendação de imóveis

Nessa fase é proposto a criação de um modelo de recomendação de imóveis tendo como base
o agrupamento dos dados com algoritmos de clusterização e a distância euclidiana. E os procedimentos realizados foram:

* Seleção de features para o modelo
* Transformar os dados em vetores
* Normalizar os dados
* Redução de dimensionalidade
* Construção do modelo de clusterização
* Contrução de uma pipeline
* Otimização do modelo de clusterização
* Criação de um recomendador de imóveis
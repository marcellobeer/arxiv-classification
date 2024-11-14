# Desenvolvimento de um Classificador de Artigos Científicos de Física Utilizando Aprendizado de Máquina e a API do ArXiv
> Autores: Marcello Beer e  Daniel de Souza Scabar


## Resumo
Este artigo apresenta o desenvolvimento de uma aplicação web que utiliza técnicas de aprendizado de máquina e processamento de linguagem natural para classificar artigos científicos de física em suas respectivas subcategorias. O sistema, implementado em Python e hospedado no Google Colab, utiliza a API do ArXiv para coletar dados, o modelo SciBERT para processamento de texto, e oferece uma interface interativa através do Streamlit.

## 1. Introdução
A classificação automática de artigos científicos é uma tarefa fundamental para organização e recuperação eficiente de informações acadêmicas. Com o crescente volume de publicações científicas, especialmente no campo da física, torna-se essencial desenvolver ferramentas que auxiliem pesquisadores a identificar e categorizar artigos relevantes.

### 1.1 Objetivos
- Desenvolver um classificador automático para artigos de física
- Implementar análise de similaridade entre artigos
- Criar uma interface web acessível e intuitiva
- Avaliar a eficácia do modelo em diferentes subcategorias da física

## 2. Referencial Teórico

### 2.1 ArXiv e Categorização de Artigos
O ArXiv é um dos principais repositórios de preprints científicos, especialmente na área de física. Sua API permite acesso programático a um vasto acervo de artigos categorizados, fornecendo uma base sólida para desenvolvimento de sistemas de classificação automática.

### 2.2 Processamento de Linguagem Natural
O projeto utiliza técnicas modernas de PLN, com destaque para:
- Transformers e arquitetura BERT
- SciBERT: modelo BERT especializado em textos científicos
- Embeddings para representação vetorial de textos

### 2.3 Aprendizado de Máquina para Classificação
A classificação é realizada utilizando:
- Modelos de classificação supervisionada
- Análise de similaridade por cosseno
- Técnicas de validação cruzada

## 3. Metodologia

### 3.1 Coleta de Dados
- Utilização da API do ArXiv para coletar artigos
- Processamento de metadados (título, resumo, categoria)
- Armazenamento em estruturas de dados eficientes

### 3.2 Processamento de Texto
- Tokenização e limpeza dos textos
- Geração de embeddings via SciBERT
- Normalização e preparação para classificação

### 3.3 Desenvolvimento do Modelo
O sistema de classificação foi implementado em múltiplas etapas:

#### 3.3.1 Preparação dos Dados
- Divisão em conjuntos de treino (80%) e teste (20%)
- Normalização dos embeddings
- Dimensionalidade dos dados: 768 features (SciBERT embeddings)

#### 3.3.2 Avaliação de Modelos
Foram implementados e comparados três diferentes classificadores:

1. **Regressão Logística**:
   - Implementação base usando sklearn
   - Otimização com regularização L2
   - Multiclass com estratégia 'one-vs-rest'

2. **Random Forest Classifier**:
   - Número de estimadores: 100
   - Critério de divisão: Gini
   - Bootstrap: True
   - Profundidade máxima: None (permitindo árvores completas)

3. **MLP (Multi-Layer Perceptron)**:
   - Arquitetura: 3 camadas (768 -> 256 -> 128 -> n_classes)
   - Função de ativação: ReLU
   - Solver: 'adam'
   - Learning rate: 'adaptive'
   - Max iterações: 1000

#### 3.3.3 Métricas de Avaliação
Para cada modelo, foram avaliadas:
- Acurácia global
- Precisão por categoria
- Recall por categoria
- F1-score
- Matriz de confusão
- Tempo de treinamento e inferência

#### 3.3.4 Análise de Similaridade
- Implementação de similaridade por cosseno
- Otimização para busca dos top-5 artigos similares
- Normalização dos scores de similaridade

### 3.4 Implementação da Interface
- Desenvolvimento da aplicação Streamlit com design amigável
- Integração com Ngrok para acesso externo

## 4. Resultados e Discussão

### 4.1 Desempenho do Classificador
Foram implementados e avaliados três modelos diferentes, com os seguintes resultados:

1. **Regressão Logística** (Melhor Modelo):
   - Acurácia de Teste: 53.86%
   - Score CV: 55.44% (±1.96%)
   - Destaques por categoria:
     - Melhor performance: Astrofísica (82% precisão e recall)
     - Física da Matéria Condensada (75% precisão)
     - Física Quântica (71% F1-score)
   - Vantagens observadas:
     - Melhor generalização entre os modelos
     - Consistência entre treino e teste
     - Performance superior em categorias bem definidas

2. **Random Forest**:
   - Acurácia de Teste: 42.95%
   - Score CV: 46.00% (±1.95%)
   - Performance por categoria:
     - Astrofísica: 79% F1-score
     - Física da Matéria Condensada: 70% F1-score
     - Performance inferior em HEP-PH (17% F1-score)

3. **Rede Neural (MLP)**:
   - Acurácia de Teste: 52.41%
   - Score CV: 54.20% (±0.99%)
   - Resultados notáveis:
     - Boa performance em Astrofísica (79% F1-score)
     - Física Quântica (71% F1-score)
     - Maior estabilidade entre as categorias

#### Análise Detalhada do Melhor Modelo (Regressão Logística)
- **Categorias com Melhor Performance**:
  1. Astrofísica (astro-ph): 82% precisão e recall
  2. Física da Matéria Condensada (cond-mat): 75% precisão
  3. Física Quântica (quant-ph): 70% precisão

- **Categorias com Desafios**:
  1. Física de Altas Energias - Fenomenologia (hep-ph): 31% F1-score
  2. Física Nuclear - Teoria (nucl-th): 34% F1-score
  3. Física de Altas Energias - Teoria (hep-th): 35% F1-score

### 4.2 Análise de Similaridade
- **Performance do Sistema**:
  - Eficácia na identificação de artigos relacionados
  - Correlação positiva com categorias preditas

### 4.3 Limitações 
  - Máximo de 512 tokens por abstract
  - Necessidade de conexão estável para acesso via Ngrok

## 5. Conclusão

O desenvolvimento deste classificador de artigos científicos de física demonstrou bons resultados, com a Regressão Logística emergindo como a abordagem mais eficaz entre os modelos testados. A performance superior em categorias bem estabelecidas como Astrofísica (82% de precisão) e Física da Matéria Condensada (75% de precisão) sugere que estas áreas possuem características linguísticas mais distintivas em seus abstracts. Por outro lado, o desempenho mais modesto em algumas subcategorias de Física de Altas Energias reflete a natural sobreposição e interdisciplinaridade destes campos. Estes resultados não apenas validam a viabilidade de classificação automática de artigos científicos, mas também oferecem insights interessantes sobre as fronteiras temáticas entre diferentes áreas da física, contribuindo para uma melhor compreensão da organização do conhecimento neste campo.


## 6. Referências

1. ArXiv API Documentation. Disponível em: https://lukasschwab.me/arxiv.py/arxiv.html

2. Pyarasani, J. (2023). Building a Text Classification System for News Articles: A Comprehensive Guide. Medium. Disponível em: https://medium.com/@JyotsnaPyarasani/building-a-text-classification-system-for-news-articles-a-comprehensive-guide-10a99e8e862d

3. ArXiv Category Taxonomy. Disponível em: https://arxiv.org/category_taxonomy

4. EPS Libraries Berkeley. ArXiv API Tutorial. Disponível em: https://colab.research.google.com/github/EPS-Libraries-Berkeley/volt/blob/main/Search/arxiv_api.ipynb

5. Ngrok Documentation. Disponível em: https://ngrok.com/

6. Topic Model LDA. Kaggle. Disponível em: https://www.kaggle.com/code/honggiangtrnh/topic-model-lda/input

7. PyPI - ArXiv Package. Disponível em: https://pypi.org/project/arxiv/

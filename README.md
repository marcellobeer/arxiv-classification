# Classificador de Artigos de Física ArXiv 📚
> Autores: Marcello Beer e Daniel de Souza Scabar
## Descrição
Uma aplicação que utiliza aprendizado de máquina para classificar artigos de física do ArXiv e encontrar papers similares. O sistema analisa o resumo (abstract) do artigo e prediz sua categoria dentro da física, além de identificar artigos semelhantes no banco de dados.

# Apresentação
🎥 https://www.youtube.com/watch?v=8zKrlLhK9kM

## Documentação Detalhada
Para uma compreensão aprofundada do projeto, consulte o arquivo `ARTICLE.md`, que contém:
- Fundamentação teórica completa
- Metodologia detalhada
- Análise dos resultados
- Referências bibliográficas
  
## Funcionalidades
- Classificação automática de artigos em 12 categorias da física
- Análise de similaridade com outros papers
- Visualização das probabilidades de classificação
- Interface web intuitiva via Streamlit
- Implementação em Google Colab com acesso via Ngrok

## Categorias de Física Analisadas
- Astrophysics (astro-ph)
- Condensed Matter (cond-mat)
- General Relativity and Quantum Cosmology (gr-qc)
- High Energy Physics - Experiment (hep-ex)
- High Energy Physics - Lattice (hep-lat)
- High Energy Physics - Phenomenology (hep-ph)
- High Energy Physics - Theory (hep-th)
- Mathematical Physics (math-ph)
- Nuclear Experiment (nucl-ex)
- Nuclear Theory (nucl-th)
- Physics (misc.)
- Quantum Physics (quant-ph)

## Tecnologias Utilizadas
- Python 3
- Google Colab (ambiente de desenvolvimento)
- Streamlit (interface web)
- PyTorch e Transformers (SciBERT para processamento de texto)
- Scikit-learn (classificação)
- ArXiv API (coleta de dados)
- Ngrok (exposição da aplicação web)

## Como Usar
1. Abra o notebook no Google Colab
2. Execute todas as células do notebook
3. Aguarde a URL do Ngrok ser gerada
4. Acesse a aplicação através da URL fornecida
5. Cole o resumo (abstract) do artigo no campo de texto
6. Clique em "Analyze Paper" para obter os resultados

## Estrutura do Projeto
O projeto está organizado em um notebook Jupyter com as seguintes seções:
1. Instalação de dependências
2. Importação de bibliotecas
3. Configurações e definições de classes
4. Coleta e processamento de dados do ArXiv
5. Treinamento do modelo
6. Implementação da interface Streamlit
7. Configuração do Ngrok

## Arquivos Gerados
- `physics_classifier.pkl`: Modelo treinado para classificação
- `paper_embeddings.npy`: Embeddings dos papers processados
- `papers_df.pkl`: Dataset com informações dos artigos
- `streamlit_app.py`: Código da interface web

## Limitações
- O acesso à aplicação via Ngrok tem duração limitada
- Necessário reexecutar o notebook para uma nova sessão
- Modelo treinado com dados disponíveis até a data de desenvolvimento

## Autor
[Seu Nome]

## Licença
Este projeto está sob a licença MIT.

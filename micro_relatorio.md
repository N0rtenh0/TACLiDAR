## 1. Identificação do Projeto

- Processamento de MDT com RVT para Análise de Relevo
- Trabalho feito por: André Rodrigues a041851 e Marta Teixeira a042166
- Data de Entrega: 12/1/2024

## 2. Objetivos e Contexto

- **Breve Descrição:**
    - Este projeto visa processar um Modelo Digital de Terreno (MDT) para gerar análises da inclinação (slope), sombreado (hillshade) e Sky View Factor (SVF), utilizando a biblioteca RVT no Python.
- **Justificativa/Contexto:**
    - A análise de MDT é essencial em diversos campos como planeamento urbano, agricultura e gestão de recursos hídricos, sendo este projeto uma aplicação prática desses conceitos.


## 3. Atividades Desenvolvidas

- **Tecnologias e Ferramentas Utilizadas:**
    - Python 3.10, bibliotecas rvt, rasterio, numpy, matplotlib e time.
- **Ambiente de desenvolvimento:** 
    - Jupyter Notebook e execução local.

- **Descrição Sintética das Tarefas:**
    - Tarefa A: Configuração do ambiente e carregamento do MDT.
    - Tarefa B: Desenvolvimento de funções para processar a inclinação, sombreado e Sky View Factor em blocos menores.
    - Tarefa C: Implementação de guardar os resultados em arquivos GeoTIFF.
    - Tarefa D: Visualização dos resultados processados e ajustes finais.

## 4. Contributos de Cada Elemento do Grupo

- **Marta Teixeira:**
    - Desenvolveu as funções de cálculo da inclinação e sombreado em blocos menores.
    - Implementou a forma de guardar os resultados em formato GeoTIFF.

- **André Rodrigues:**
    - Criou a função para processamento do Sky View Factor em blocos menores.
    - Elaborou a parte de visualização gráfica e ajustou os parâmetros para otimizar a execução.

## 5. Organização e Metodologia de Trabalho

- **Planeamento e Cronograma:**
    - Dividimos o trabalho de forma equitativa ao longo de duas semanas, com foco em tarefas específicas para cada aluno.
- **Comunicação e Articulação:**
    - Falamos através de mensagens e reuniões online para discutir o progresso e resolver dúvidas.
- **Forma de Integração do Código:**
    - Armazenamos o projeto em uma pasta compartilhada  para facilitar o acesso e a integração.

## 6. Principais Dificuldades e Aprendizagens

- **Dificuldades Encontradas:**
    - Aprender a utilizar a biblioteca RVT e lidar com erros na instalação, optando por instalar pelo conda.
    - Processar grandes MDTs sem comprometer a memória do sistema.
- **Aprendizagens e Evolução:**
    - Otimização de processamento por blocos para grandes volumes de dados.
    - Geração de arquivos GeoTIFF e técnicas de visualização em Python.

## 7. Conclusão e Próximos Passos

- **Estado Final do Projeto:**
    - O projeto é funcional, gerando os três resultados esperados (slope, hillshade e SVF) com eficiência.
- **Sugestões de Futuro:**
    - Implementação de uma interface gráfica para facilitar o uso por usuários não técnicos.
    - Adaptação do código para suportar diferentes formatos de entrada de MDT.

## 8. Referências

- **Documentação do Rasterio:** https://rasterio.readthedocs.io/
- **Documentação do RVT:** https://rvt-py.readthedocs.io

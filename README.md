# BaixarDadosDoENEM
Os arquivos a seguir baixam de forma automática os arquivos do ENEM, extraem e permitem filtrar apenas as informações necessárias e armazená-las em outro arquivo '.csv'.

Sei da existência de bibliotecas mais robustas para fazer isso de forma mais simples. Porém, elas tendem a carregar tudo na memória ram para depois analisar. Meu computador não suporta tantos dados na memória.
Tendo isso em vista, decidi filtrar de uma forma mais arcaica os dados que queria para, mais tarde, analisar utilizando tais bibliotecas.

### Utilização
Faça o download do arquivo 'main.py', 'FiltrarDadosBaixados.py' e 'BaixarEExtrair' e coloque-os todos em uma mesma pasta. Após isso, execute o arquivo 'main.py' e siga os comandos do terminal.

Quando for necessário filtrar as informações, será aberta uma janela onde o usuário seleciona apenas as informações desejadas. Nesta janela, selecione os campos desejados (para mais informações, consulte o dicionário disponibilizado com os arquivos do ENEM) e feche a janela. O programa terminará criando um arquivo com as colunas selecionadas do arquivo original. Este arquivo ficará disponível em Arquivos/DadosFiltrados/ANOESCOLHIDO.csv.

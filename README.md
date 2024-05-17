# dataanalysis-ebac
# Análise de Preços da Gasolina em São Paulo

Este repositório contém um projeto de análise de dados que investiga o preço médio de venda da gasolina na cidade de São Paulo nos primeiros 10 dias de julho de 2021.

## Configuração

O projeto foi desenvolvido utilizando o Jupyter Notebook no Google Colab. Para replicar o ambiente e executar os códigos, siga as instruções. Utilizando as bibliotecas do matplotlib, seaborn e pandas.

### Clone o projeto do GitHub para a sua máquina local:

```
!git clone https://github.com/IvanTrigueiro/dataanalysis-ebac
%cd /content/dataanalysis-ebac/
```

### Autenticação

Para configurar o git com suas credenciais, utilize o seguinte código

```python
import os
from getpass import getpass

username = "SeuNomeDeUsuárioDoGit" # substitua pelo seu nome de usuário do git
usermail = getpass('Digite seu email do GitHub:')
usertoken = getpass('Digite seu token do GitHub:')

os.environ["GITHUB_USER"] = username
os.environ["GITHUB_MAIL"] = usermail
os.environ["GITHUB_TOKEN"] = usertoken

!git config --global user.name "${GITHUB_USER}"
!git config --global user.email "${GITHUB_MAIL}"
```



Lembre-se de substituir **"SeuNomeDeUsuárioDoGit"** pelo seu nome de usuário do GitHub e inserir suas credenciais quando solicitado.




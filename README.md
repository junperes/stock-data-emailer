# Sobre

Bot que a partir de uma carteira de ações listada no Excel utiliza a biblioteca pandas_datareader para extrair dados dos último n dias, sendo n o valor de entrada da função. A partir desses dados calcula o valor de hoje e o valor mínimo, médio e máximo do fechamento ajustado dos n dias.

Também extrai as cotações do dólar, euro e criptomoedas usando uma API.

Por fim uma função envia todas essas informações por email.

## Instalação:

Dentro da pasta do projeto, inicie um ambiente virtual:

Lunix or Mac
```
python3 -m venv .env
source env/bin/activate
```
Windows
```
py -m venv .env
.\env\Scripts\activate
```

### Dependências:
```
pip install -r requirements.txt
```

## Configurações:

O cotacoes.py é um programa independente, possui duas funções: 
- carteira(n_dias) que recebe como parâmetro os dias retroativos, e tem por padrão a data final como hoje. Para cada ação da carteira a função retorna o ajuste calculado de hoje, o valor mínimo, médio e máximo dos n dias.
- moeda() não recebe nenhum parâmetro e retorna o valor das cotações do dólar, euro e criptomoeda para o instante que o programa é executado.

O cotacoesHTML.py é semelhante ao cotacoes.py porém possui ajustes de HTML para formatar o envio do email.

O robotmail.py tem como função o send_mail(message1, message2) que recebe dois parâmetros, seriam as funções carteira e moeda. E envia os resultados para o email. 

Para que o email seja enviado precisa ser alterado no código os campos de "sender_email", "receiver_email" e "password". O "sender_email" precisa ter nas configurações de segurança do Google uma senha criada para app, caso contrário o Google impede o envio do email.

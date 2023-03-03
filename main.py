import pandas as pd
from twilio.rest import Client

account_sid = 'AC14ca841641345048c5ada574fb99653a'
auth_token = 'dfc34dcba944a87de17e3bea3c2d53bc'
client = Client(account_sid, auth_token)

# imports que deveram ser feitos:
# pandas, openpyxl e twilio

# Passo a Passo de solução da aplicação

# Abrir os arquivos do exel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

number = 5551997641319

for mes in lista_meses:
    # tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    tabela_vendas = pd.read_excel('./Assets/{}.xlsx'.format(mes))
    # Para cada arquivo:
    # Verificar se algum valor da coluna 'Vendas' daquele arquivo é maior que 55.000
    if (tabela_vendas['Vendas'] > 55000).any():
        # Se for maior do que 55.000 -> envia um SMS com o nome, o mês e as vendas do vendedor
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendas'].values[0]
        #print(f'No mes de {mes} o vendedor {vendedor} arrecadou mais de 55.000 com a quantidade de vendas: {vendas}')
        print('No mes de {} o vendedor {} arrecadou mais de 55.000 com a quantidade de vendas: {}'.format(mes, vendedor, vendas))
        message = client.messages.create(
                     body='No mes de {} o vendedor {} arrecadou mais de 55.000 com a quantidade de vendas: {}'.format(mes, vendedor, vendas),
                     from_='+12708354602',
                     to='+5551998955866'
                 )

        print(message.sid)

# Caso o valor seja menor que o desejado ou se n houver um vendedor que alcançou o valor, o programa n retornará nd








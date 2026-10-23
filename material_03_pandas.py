import pandas as pd
import shutil, os, datetime
print('\033c')

def teste_criação_df(Lista_1, Lista_2, Lista_3):
    pessoas = {
        "nome": Lista_1,
        "idade": Lista_2,
        "sexo": Lista_3,
    }
    df = pd.DataFrame(pessoas)
    print(df, '\n')
    aniversario = pd.Series([pd.Timestamp("1998-01-15"), pd.Timestamp("1993-05-20"), pd.Timestamp("1988-09-10")])
    df["aniversario"] = aniversario
    print(df.head(), '\n')
    print(df.describe(), '\n')
    print(df.dtypes, '\n')
    teste = pd.DataFrame(Lista_1, Lista_2)
    print(teste)
    teste['sexo'] = Lista_3
    print(teste)
    print(type(teste))
    print(type(df))
    print(type(aniversario))



# leitura
def leitura(arq):
    df = pd.read_csv(arq, delimiter=',')

    print('Os primeiros 10 vendas \n', df.head(10), '\n')
    print('Informações das colunas \n', df.info(), '\n')
    series = df['CPF']
    df.index = series
    print('Agora tendo o indice o cpf \n', df.tail(10), '\n')
    return df



def filtros(df):
    # Filtro de dados
    lista = ['Gomes de Rezende', 'da Rosa de Novais', 'Alves', 'Cavalcante do Amparo']
    df_cidade_e_idade = df[(df['CIDADE'].isin(lista)) & (df['IDADE'] < 30)]
    df_comissao_ou_vendedor = df[(df['COMISSAO_FLOAT'] > 10) | (df['VENDEDOR'] == 6498)]
    print(df_cidade_e_idade[['NOME', 'CIDADE', 'IDADE', 'VALOR_NOTA']].head())
    print(df_comissao_ou_vendedor[['NOME', 'CIDADE', 'VENDEDOR', 'COMISSAO', 'VALOR_NOTA']].head())

    return df, df_cidade_e_idade, df_comissao_ou_vendedor


# exportação
def exportação(df, df_cidade_e_idade, df_comissao_ou_vendedor):
    df.to_parquet(r'./output/vendas(bruto)_falsa.pqt', index=False)
    df_cidade_e_idade.to_json(r'./output/vendas(bruto)_falsa.json', orient='records', lines=True, index=False)
    df_comissao_ou_vendedor.to_excel(r'./output/vendas(bruto)_falsa.xlsx', index=False)



# conversa de valores
def convertar_dados_fin_num(df, colun):
    df[colun] = pd.to_numeric(df[colun].apply(lambda x: x.replace('R$', '')).apply(lambda x: x.replace(',', '.')).astype('float'))
    print(df[colun].head(),'\n')


# Excel
def Excel_testes(arq):
    df = pd.read_excel(arq)
    print(df.head())

    colunas_lista = ['Nota_1', 'Nota_2', 'Nota_3', 'Nota_4']
    df[colunas_lista] = df[colunas_lista].apply(pd.to_numeric)
    df['media'] = df[colunas_lista].mean(axis=1)

    print(df.head(),'\n')

    with pd.ExcelWriter(arq, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
        df.to_excel(writer, index=False, sheet_name="Media_notas")

    print('Excel adicionado')
    return df

def result(df, caminho, vlr_ap=7):
    if(os.path.exists(caminho)):
        os.remove(caminho)

    shutil.copy('Material 23 - Notas.xlsx', caminho)

    df['Aprovado'] = df['media'].apply(lambda x: 'Sim' if x > vlr_ap else "Nao")
    
    excel = pd.ExcelWriter(caminho, engine='openpyxl', mode='a', if_sheet_exists='replace')
    df.to_excel(excel, index=False, sheet_name="Media_notas")
    print(df)


teste_criação_df(["João", "Maria", "Pedro", "Ana"], [25, 30, 35, 28],["M", "F", "M", "F"])

df = leitura(r'./output/Vendas (Bruto)_falsa.csv')
df, df1, df2 = filtros(df)
exportação(df, df1, df2)
convertar_dados_fin_num(df, 'VALOR_NOTA')

df = Excel_testes('Material 21 - Notas.xlsx')
result(df, r'./output/Material 23 - Notas.xlsx')

def localizacao_loc(arq):
    df = pd.read_excel(arq)

    #print(df.head())
    #df.index = df["NOTA_FISCAL"] # dará erro na priocura dos indices a baixo

    print(df.loc[0], '\n')
    df_10_30 = df.loc[10:30] # ira retornar de 10 - 30
    print(df_10_30, '\n')
    lista_indice = [10, 12, 55, 88, 32, 11]
    print(df.loc[lista_indice], '\n')

    df_filter_VendedorE = df.loc[df['VENDEDOR'] == 'Vendedor_E']
    print(df_filter_VendedorE.head(), '\n')
    df_filter_VendedorA_500 = df.loc[(df['VENDEDOR'] == 'Vendedor_A') & (df['VALOR_NOTA'] >= 500)]
    print(df_filter_VendedorA_500.head(), '\n')

    df_silvas = df.loc[df['NOME'].str.contains('Silva', regex=False)]
    print(df_silvas, '\n')

    df.index = df["NOTA_FISCAL"]
    print(df.loc[764787])

def localizacao_iloc(arq):
    df = pd.read_excel(arq)
    #print(df)
    df.index = df["CPF"]

    print(df.iloc[0])

    print(df.iloc[10:30]) # irá retornar de 10 a 29

    print(df.iloc[-10:-1]) # ultima linha

    df_nome_a_cidade = df.iloc[:, 1:4]
    print(df_nome_a_cidade)

    df_10_30 = df.iloc[10:30, :]
    print(df_10_30)

    df.iloc[10, 1] = "Carlitos Substituido"
    print(df.iloc[10])

    print(df_10_30.iloc[1:10])
    df_10_30.iloc[10, 1] = "Carlitos Substituido"
    print(df_10_30[9:12])
    ...

localizacao_loc("Material 24 - Vendas.xlsx")
localizacao_iloc("Material 24 - Vendas.xlsx")

def analise(arq):
    df = pd.read_csv(arq, sep=';', encoding='utf-8')

    print(df.head())

    print(df[df.isna().any(axis=1)])
    print(df.isna().sum())

    df['DATA E HORA COMPRA'] = df['DATA E HORA COMPRA'].fillna(datetime.datetime(1900,1,1).strftime("%d/%m/%Y %H:%M:%S" ))

    df["MES"] = df['DATA E HORA COMPRA'].str[3:5]
    df["REFERENCIA"] = df['DATA E HORA COMPRA'].str[6:10] + df['DATA E HORA COMPRA'].str[3:5]
    print(df.head())

    df.to_excel(r'.\output\Material 27 - Vendas.xlsx')
    print("Concluido a primeira parte")

def analise2(arq):
    df = pd.read_excel(arq)

    df['PREÇO UNITÁRIO'] = df['PREÇO UNITÁRIO'].str.replace(',', '.')
    df['PREÇO UNITÁRIO'] = pd.to_numeric(df['PREÇO UNITÁRIO'])
    
    df['TOTAL'] = df['QUANTIDADE'] * df["PREÇO UNITÁRIO"]

    df_por_mes = df.groupby('MES')['TOTAL'].sum()
    df_por_mes = df_por_mes.apply(formatar_em_reais)
    print(df_por_mes)

    df_por_referencia = df.groupby('REFERENCIA')['TOTAL'].sum()
    df_por_referencia = df_por_referencia.apply(formatar_em_reais) 
    print(df_por_referencia)
    print(type(df_por_referencia))

    total = 0
    diferenca = 0
    limite = 5000

    for registro in df['TOTAL']:
        if registro >= limite:
            total += registro
        else:
            diferenca += registro

    print(f'O total de faturamento a cima de {formatar_em_reais(limite)} é de {formatar_em_reais(total)}')
    print(f'O total de faturamento a baixo de {formatar_em_reais(limite)} é de {formatar_em_reais(diferenca)}')

    df.to_excel(r'.\output\Materia 27 - Vendas - Total.xlsx')

def formatar_em_reais(pValor):
    return f'R$ {pValor:,.2f}'.replace(',', '#').replace('.', ',').replace('#', '.')


analise("Material 26 - Vendas.csv")
analise2(r".\output\Material 27 - Vendas.xlsx")
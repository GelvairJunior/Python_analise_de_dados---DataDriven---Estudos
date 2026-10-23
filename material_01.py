import math as m
import random as rd
import time
import datetime as dt
import os

def math_teste():
    print('\033c')
    print("math.fabs(-5.66):", m.fabs(-5.66))
    print("math.pi:", m.pi)
    print("math.trunc(math.pi):", m.trunc(m.pi))
    print("math.ceil(math.pi):", m.ceil(m.pi))
    print("math.floor(math.pi):", m.floor(m.pi))
    print("math.comb(25,3):", m.comb(25,3))
    print("round(math.sqrt(1888), 2):", round(m.sqrt(1888), 2))
    print("round(math.cbrt(300),2):", round(m.cbrt(300),2))
    print("math.pow(9, 2):", m.pow(9, 2))
    print("math.nan:", m.nan)
    venda_inicial = 100000
    venda_final = 150000
    periodo_anos = 2
    cagr = (m.pow(venda_final/venda_inicial, 1/periodo_anos) - 1)*100
    print(f"Crescimento percentual anual composto(CAGR): {cagr:.2f}%")

def random_test():
    print('\033c')
    list_random = rd.sample(range(1, 100), 10)
    print(rd.randint(1, 100), end=" ")
    print(rd.randrange(0, 100, 5))
    print("Escolhendo um item aleatório",rd.choice(['Item A', 'Item B', "Item C"]))
    print("lista gerada aleatóriamento:", list_random)
    print("lista gerada aleatóriamento (classificada):", sorted(list_random))
    list_random.sort()
    print("lista gerada aleatóriamento (classificada):", list_random)


    print("N1:", round(rd.random(),3))
    state = rd.getstate()
    print("N2:", round(rd.random(),3))
    rd.setstate(state=state)
    print("N3:", round(rd.random(),3), '\n')
    rd.seed(1902)
    valores = [round(rd.random(),2) for n in range(30)]
    print("30 numeros aleatórios com seed 1902:", valores,'\n')

    #simulacao com numeros aleatórios
    dias = 30
    vendas_diarias = [rd.randint(500, 1200) for n in range(dias)]
    print(("vendas diariamente:").ljust(50), vendas_diarias, )
    print(("total vendido no mes:").ljust(50),"R$", sum(vendas_diarias))
    print(("media vendas no mes:").ljust(50), "R$",round(sum(vendas_diarias)/dias,2))
    print(("maior venda do mes:").ljust(50), "R$",max(vendas_diarias))
    print(("menor venda do mes:").ljust(50), "R$",min(vendas_diarias))

    ##simulacao para frente
    dias_a_frente = 15
    valores_vendas_frente = [(sum(vendas_diarias)/dias)+rd.uniform(-100, 100) for n in range(dias_a_frente)]
    print(("vendas diariamente nos proximos 15 dias:").ljust(50), [round(n,2) for n in valores_vendas_frente])

def time_teste():
    print('\033c')
    tempo = time.localtime()
    print(tempo)

    tempo_inicial = time.localtime()
    tempo_de_parada = time.mktime(tempo_inicial)
    tempo_de_parada += 5
    tempo_fim = time.localtime(tempo_de_parada)

    while tempo_inicial != tempo_fim:
        time.sleep(1)
        tempo_inicial = time.localtime()
        result = time.strftime('%H:%M:%S %p', tempo_inicial)
        print(result)


    # quanto tempo dura fazer isso
    tempo_inicial = time.time()
    import teste_estresse
    teste_estresse
    print(teste_estresse.frase_aleatoria_com_bigram_makarov)
    tempo_final = time.time()
    print(f"{tempo_final - tempo_inicial:.2f} segundos para executar o teste_estresse.py")

def datatime_teste():
    print('\033c')
    agora = dt.datetime.now()

    data_cadastro = [dt.datetime(rd.randint(2023, 2025), rd.randint(1, 12), rd.randint(1, 29), rd.randint(1, 23), rd.randint(1, 59), rd.randint(1, 59)), 
                dt.datetime(rd.randint(2023, 2025), rd.randint(1, 12), rd.randint(1, 29), rd.randint(1, 23), rd.randint(1, 59), rd.randint(1, 59)), 
                dt.datetime(rd.randint(2023, 2025), rd.randint(1, 12), rd.randint(1, 29), rd.randint(1, 23), rd.randint(1, 59), rd.randint(1, 59)), 
                dt.datetime(rd.randint(2023, 2025), rd.randint(1, 12), rd.randint(1, 29), rd.randint(1, 23), rd.randint(1, 59), rd.randint(1, 59)), 
                dt.datetime(rd.randint(2023, 2025), rd.randint(1, 12), rd.randint(1, 29), rd.randint(1, 23), rd.randint(1, 59), rd.randint(1, 59)),]

    cliente_cadastro = ["joão", "maria", "jose", "marcia", "carla"]
    data_saida = [None, dt.datetime(2026, 1, 30, 1, 5, 32), dt.datetime(2026, 4, 30, 1, 5, 32), 
                  dt.datetime(2026, 7, 30, 1, 5, 32), None]

    for cliente, entrada, saida in zip(cliente_cadastro, data_cadastro, data_saida):
        if saida:
            tempo = (saida - entrada).days
            print(f'Cliente {cliente}, cadastrado em {entrada.strftime("%d/%m/%Y")} : {tempo} dias')
        else:
            tempo = (agora - entrada).days
            print(f'Cliente {cliente}, cadastrado em {entrada.strftime("%d/%m/%Y")} : {tempo} dias (ativo)')
    print()

    total_clientes = len(cliente_cadastro)
    clientes_cancelados = sum(1 for n in data_saida if n is not None)
    taxa_churn = clientes_cancelados / total_clientes * 100

    print(f'Taxa de churn: {taxa_churn:.2f}% \n')

    for cliente, saida in zip(cliente_cadastro, data_saida):
        if saida == None:
            print(f'{cliente} ativo até {agora}')
        else:
            print(f'{cliente} saiu em {saida}')

    fut = agora + dt.timedelta(days=50)
    print(f'utilizando timedelta {fut}')

    gta = dt.datetime(year=2026, month=11, day=19, hour=0, minute=0, second=0)
    tempo_gta = gta-agora
    print(f'tempo até o gta: {tempo_gta}')

def os_teste():
    os.system('clear' if os.name == 'posix' else 'cls')
    print('aqui vai uma lista das variaveis de ambientes:')
    for param in os.environ:
        print(f'{param}:{os.environ.get(param)}')
    os.system('clear' if os.name == 'posix' else 'cls')
    principal = os.getcwd()
    extras = 'extra'
    caminho_extra = os.path.join(principal, extras)
    arq = 'arquivo.txt'
    caminho_arq = os.path.join(principal, extras, arq)
    if os.path.exists(caminho_extra):
        if os.path.exists(caminho_arq):
            print(open(caminho_arq, "r", encoding="utf-8").readline(), '\n')
            os.remove(caminho_arq)
            os.rmdir(caminho_extra)
        else:
            open(caminho_arq, 'w', encoding='utf-8').write(fake.text(max_nb_chars=200))
            print('criado arquvio.txt \n')
    else:
        os.mkdir(extras)
        print('criado a pasta extra \n')

    print(os.path.dirname(caminho_arq), '\n')
    print(os.path.basename(caminho_arq), '\n')

    print(f'{caminho_arq} é um diretorio \n' if os.path.isdir(caminho_arq) else f'{caminho_arq} é um arquivo \n')
    os.system('dir')

math_teste()
random_test()
time_teste()
datatime_teste()
os_teste()
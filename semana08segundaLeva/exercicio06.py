def obter_resposta():
    resposta = input("Digite a resposta (sim ou não): ")
    while resposta.lower() != "sim" and resposta.lower() != "não":
        resposta = input("Resposta inválida. Digite novamente (sim ou não): ")
    return resposta.lower()

def calcular_resultados():
    total_sim = 0
    total_nao = 0

    for i in range(20):
        resposta = obter_resposta()
        
        if resposta == "sim":
            total_sim += 1
        else:
            total_nao += 1

    return total_sim, total_nao

def exibir_resultados(total_sim, total_nao):
    print("Total de pessoas que responderam sim:", total_sim)
    print("Total de pessoas que responderam não:", total_nao)

# Função principal para executar a pesquisa
def realizar_pesquisa():
    print("Pesquisa de aceitação do produto")
    print("Responda sim ou não para cada pessoa.")
    print("----------------------------------")
    
    total_sim, total_nao = calcular_resultados()
    
    print("\n--- Resultados da Pesquisa ---")
    exibir_resultados(total_sim, total_nao)

# Chamada da função principal para iniciar a pesquisa
realizar_pesquisa()

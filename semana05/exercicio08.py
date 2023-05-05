# inicializa os contadores de uso dos elevadores A, B e C
uso_elevador_a = 0
uso_elevador_b = 0
uso_elevador_c = 0

# coleta as informações de uso dos elevadores dos moradores
for i in range(10):
    elevador_utilizado = input(f"Informe qual elevador o morador {i+1} utiliza com mais frequência (A/B/C): ")

    # incrementa o contador do elevador utilizado pelo morador atual
    if elevador_utilizado == 'A':
        uso_elevador_a += 1
    elif elevador_utilizado == 'B':
        uso_elevador_b += 1
    elif elevador_utilizado == 'C':
        uso_elevador_c += 1

# calcula o total de pessoas que utiliza cada elevador
total_pessoas = uso_elevador_a + uso_elevador_b + uso_elevador_c

# exibe os totais de uso de cada elevador e suas respectivas porcentagens
print(f"Total de pessoas que usa o elevador A: {uso_elevador_a} ({(uso_elevador_a / total_pessoas) * 100:.2f}%)")
print(f"Total de pessoas que usa o elevador B: {uso_elevador_b} ({(uso_elevador_b / total_pessoas) * 100:.2f}%)")
print(f"Total de pessoas que usa o elevador C: {uso_elevador_c} ({(uso_elevador_c / total_pessoas) * 100:.2f}%)")

def distribuir_vacinas(N, doses):
    primeira_dose_total = 0
    segunda_dose_total = 0
    devolvidas_total = 0
    
    for i in range(N):
        print(f"Mês {i+1}:")
        
        devolvidas = 0
        
        # Verifica se há pessoas para receber a segunda dose
        if i >= 3 and segunda_dose_total > 0:
            pessoas_segunda_dose = segunda_dose_total
            segunda_dose_total = 0
            print(f"Vacinados com a segunda dose: {pessoas_segunda_dose}")
        
        # Verifica se há pessoas para receber a primeira dose
        elif doses[i] > 0:
            if i < N - 3:
                doses_para_primeira_dose = min(doses[i], primeira_dose_total)
                primeira_dose_total += doses_para_primeira_dose
                doses[i] -= doses_para_primeira_dose
                print(f"Vacinados com a primeira dose: {doses_para_primeira_dose}")
            
            # Caso contrário, vacina todas as doses restantes
            else:
                primeira_dose_total += doses[i]
                print(f"Vacinados com a primeira dose: {doses[i]}")
                doses[i] = 0
        
        # Calcula e imprime o número de doses devolvidas
        devolvidas = primeira_dose_total + segunda_dose_total
        print(f"Vacinas devolvidas: {devolvidas}")
        devolvidas_total += devolvidas
        
        # Atualiza o número total de doses para a segunda dose
        segunda_dose_total = primeira_dose_total
        primeira_dose_total = 0
        
        print()  # Adiciona uma linha em branco para melhorar a legibilidade
    
    # Calcula e imprime o resumo total
    print("Total:")
    print(f"Vacinados apenas com a primeira dose: {segunda_dose_total}")
    print(f"Vacinados com as duas doses: {segunda_dose_total}")
    print(f"Vacinas devolvidas: {devolvidas_total}")

# Leitura da entrada
N = int(input("Digite o número de meses: "))
doses = []
for i in range(N):
    doses.append(int(input(f"Digite o número de doses disponíveis para o mês {i+1}: ")))

# Chamada da função para distribuição das doses
distribuir_vacinas(N, doses)

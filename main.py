def calcular_ciclo(direcoes):
    tempo_verde = 10
    tempo_amarelo = 3
    tempo_vermelho = 13
    
    ciclo_total = 0
    esperas = {}
    
    for direcao in direcoes:
        tempo_na_direcao = tempo_verde + tempo_amarelo
        tempo_espera = tempo_vermelho
        
        ciclo_total += tempo_na_direcao
        esperas[direcao] = tempo_espera
        
    maior_espera = max(esperas, key=esperas.get)
    
    return {
        "ciclo_total": ciclo_total,
        "maior_espera": maior_espera,
        "tempo_espera_maior": esperas[maior_espera]
    }

if __name__ == "__main__":
    lista_direcoes = ["Norte", "Leste", "Sul", "Oeste"]
    resultado = calcular_ciclo(lista_direcoes)
    print(f"Ciclo total: {resultado['ciclo_total']}s")
    print(f"Direção com mais espera: {resultado['maior_espera']} ({resultado['tempo_espera_maior']}s)")
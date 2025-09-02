
def calc_combustivel(distancia_percorrida, consumo_medio):
    return distancia_percorrida / consumo_medio


tempo_gasto = float(input())
velocidade_media = float(input())
consumo_medio = float(input())

distancia_percorrida = tempo_gasto * velocidade_media
combustivel_gasto = calc_combustivel(distancia_percorrida,consumo_medio)

print(combustivel_gasto)
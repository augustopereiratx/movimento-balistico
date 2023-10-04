from math import sin, cos, sqrt
import sympy as sp

def main():
    # Declaração inicial de variáveis
    g = 9.8
    y0 = input("Digite o valor de y0: ")
    y = input("Digite o valor de uma altura diferente de 0: ")
    v0 = input("Digite o valor do módulo do vetor: ")
    alfa = input("Digite o ângulo do vetor em relação ao solo: ")
    td = input("Digite um tempo (em segundos) qualquer após o lançamento: ")
    
    # Mudar para números
    y0 = float(y0)
    y = float(y)
    v0 = float(v0)
    alfa = float(alfa)
    td = float(td)

    # Decompor o vetor
    v0x = cos(alfa) * v0
    print("Velocidade inicial x:",v0x)
    v0y = sin(alfa) * v0
    print("Velocidade inicial y:",v0y)

    # Calcular tempo em que chega no ápice y
    tymax = v0y/g
    print("Tempo no ápice de y:",tymax)


    # Tempo no ar é igual a 2 * tempo de subida
    tnoar = tymax * 2
    print("Tempo no ar:",tnoar)

    # Y máximo
    ymax = y0 + v0y*tymax - g*(tymax**2)*0.5
    print("Valor de y no ápice:",ymax)

    # X máximo
    xmax = v0x*tnoar
    print("Valor de x no ápice:", xmax)

    # vx, vy e |v->| na posição hmax
    vxapice = v0x
    print("Velocidade x na posição hmax:",vxapice," * i")

    vyapice = ymax/tymax
    print("Velocidade y na posição hmax:",vyapice," * j")

    moduloapice = (cos(alfa)*vxapice + sin(alfa)*vyapice)
    print("Módulo |v->| na posição hmax:",moduloapice)

    # vx, vy e |v->| quando atinge o solo
    vxsolo = v0x
    print("Velocidade x quando atinge o solo:",vxsolo," * i")

    vysolo = (y0 + v0y*tnoar - g*(tnoar**2)*0.5)/tnoar
    print("Velocidade y quando atinge o solo:",vysolo," * j")

    modulosolo = (cos(alfa)*vxsolo + sin(alfa)*vysolo)
    print("Módulo |v->| quando atinge o solo:",modulosolo)

# Executar
main()
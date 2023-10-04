from math import sin, cos, sqrt, radians

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
    alfa = radians(float(alfa))
    td = float(td)

    # Decompor o vetor
    v0x = cos(alfa) * v0
    print("Velocidade inicial x:",v0x)
    v0y = sin(alfa) * v0
    print("Velocidade inicial y:",v0y)

    # Y máximo
    if(v0y != 0):
        ymax = (v0y**2/g)/2
    else:
        ymax = y0
    print("Valor de y no ápice:",ymax)

    # Calcular tempo em que chega no ápice y
    tymax = v0y/g
    print("Tempo no ápice de y:",tymax)


    # Tempo no ar é igual a 2 * tempo de subida
    if(tymax != 0):
        tnoar = tymax * 2
    else:
        tnoar = sqrt(((2*y0)/g))
    print("Tempo no ar:",tnoar)

    # X máximo
    xmax = v0x*tnoar
    print("Valor de x no ápice:", xmax)

    # vx, vy e |v->| na posição hmax
    vxapice = v0x
    print("Velocidade x na posição hmax:",vxapice," * i")

    vyapice = 0.0
    print("Velocidade y na posição hmax:",vyapice," * j\nNo hmax, vy é sempre igual a 0, pois é o momento em que a gravidade vence a velocidade vertical do objeto.")

    moduloapice = vxapice**2 + vyapice**2
    moduloapice = sqrt(moduloapice)
    print("Módulo |v->| na posição hmax:",moduloapice)

    # vx, vy e |v->| quando atinge o solo
    vxsolo = v0x
    print("Velocidade x quando atinge o solo:",vxsolo," * i")

    vysolo = v0y-g*tnoar
    print("Velocidade y quando atinge o solo:",vysolo," * j")

    modulosolo = vxsolo**2 + vysolo**2
    modulosolo = sqrt(modulosolo)
    print("Módulo |v->| quando atinge o solo:",modulosolo)

    xtd = (v0x*td)
    print("x(td): ",xtd,"m")

    ytd = (y0 + v0y*td - (g*(td**2))/2)
    print("y(td): ",ytd,"m")

    vxtd = v0x
    print("vx(td): ",vxtd,"m/s")
    
    vytd = v0y - g*td
    print("vy(td): ",vytd,"m/s")

    modulotd = sqrt(vxtd**2+vytd**2)
    print("módulo(td): ",modulotd,"m/s")
    

# Executar
main()
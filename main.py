# Código de inscrição para o projeto CrossBots

def radianos_graus(rad):
    '''Recebe um ângulo em radianos como parâmetro e retorna
    o correspondente em graus arredondado em uma casa decimal.'''
    return round(rad * 180, 1)


def converter(horas):
    '''Recebe um valor de horas e retorne uma lista com meses,
    semanas, minutos , segundos e milisegundos.'''
    convertido = [int(horas / 720), int(horas / 168), horas * 60, horas * 3600, horas * 3600000]
    return convertido


def repeti(item, n):
    '''Retorna uma lista que repete n vezes o Item passado no parâmetro.'''
    repetido = []
    for vezes in range(0, n): repetido.append(item)  # Repete append n vezes
    return repetido


def conta_uns(num_dec):
    '''Retorna o número de uns na representação binária do número passado no parâmetro.'''
    binario = bin(num_dec)  # Converte num_dec para uma string binária
    return int(binario.count("1"))  # Conta quantos uns há na string e retora como int


def distancia(c1, c2):
    '''Retorna a distância entre duas coordenadas no plano cartesiano.'''
    # Calcula a distância através do teorema de pitágoras d=raiz(a^2+b^2)
    a = (c1[0] - c2[0]) ** 2
    b = (c1[1] - c2[1]) ** 2
    return round((a + b) ** (1/2),2)


def CrossBots(num):
    '''Retorna Cross caso num seja múltiplo de 3, Bots se for de 5, concatenado
     se for de ambos ou num caso não seja de nenhum'''
    cross = ""
    bots = ""
    if (num % 3 != 0 and num % 5 != 0): return num
    if (num % 3 == 0): cross = "Cross"
    if (num % 5 == 0): bots = "Bots"
    return cross + bots

# Considere n = 1000

def lista1(): # O(n)
    lista = []
    for i in range(1000):
        lista += [i]

    return lista

def lista2(): # O(1000) -> O(n)
    return range(1000)

# Muitas vezes vale utilizar uma estrutura pronta pois entrega o que precisamos
# em poucos passos e de modo otimizado, uma vez que os engenheiros focam nisso

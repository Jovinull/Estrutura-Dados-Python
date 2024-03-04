# Constant - O(1)
def constant(n):
    print(n[0])

# Linear - O(n)
def linear(n):
    for i in n:
        print(i)

# Quadratic - O(n^)
def quadratic(n):
    for i in n:
        for j in n:
            print(i, j)
        print('---')

# Combination
def combination(n):
    print(n[0]) # O(1)

    for i in range(5): # O(5)
        print(i)

    for i in n: # O(n)
        print(i)

    print('Python') # \/
    print('Python') # O(3)
    print('Python') # /\

####################################
#        Calculo dos Passos        #
# O(1) + O(5) + O(n) + O(n) + O(3) #
#       O(9) + O(2n) -> O(n)       #
#                                  #
#  Constantes são insignificantes  #
#  perto de infinitos como (n) por #
#        isso ignoramos elas       #
####################################

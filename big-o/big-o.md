# Notação Big-O (Grande O)

Descreve o desempenho ou a complexidade de um algoritmo em termos de sua eficiência, especialmente em relação ao crescimento do tempo de execucação ou uso de recursos à medida que o tamanho da entrada aumenta.

É o pior caso de desempenho de um algoritmo em relção a otamanho da entrada.

O Big-O não fornece uma medida precisa do desempenho absoluto mas sim uma visão de como o desempenho se comporta à medida que o tamanho da entrada aumenta, isso é importante para entender a escalabilidade dos algoritmos e escolher a melhor solução para um problema específico.

- Como comparar dois algoritmos
- Comparação objetiva entre algoritmos
- Considera diferenças entre poder de processamento, sistema operacional, linguagem de programação
- O quanto a "complexidade" do algoritmo aumenta de acordo com as entrada

## Exemplo do Ponto 1:

Observe os códigos no arquivo "ponto-1"

Comparando no meu computador com o comando %timeit para verificar o tempo podemos ter uma noção da diferença entre os dois, a segunda função é superior nesse quesito, isso acontece pois ela possui uma menor quantidade de passos
- **OBS:** Passos é a quantidade de operações que um código ira fazer.

Nossa primeira função é classificada como O(n) pois para cada entrada ela realiza uma execução já o segundo realiza 3 passos indepedentemente da quantidade de entradas por isso é O(3).

Agora vamos calcular os passos para a função 1:
- Atribui a variavel (1)
- Para cada incremento (1) que é n
- Total de Passos: 1 + n

Agora para a função 2:
- Multiplicação (1)
- Soma (1)
- Divisão (1)
- Total de Passos: 3

**OBS:** A função 2 não aumenta a quantidade de passos com o aumento da entrada, tem um número fixo de passos. Já a função 1 a quantidade de passos aumenta conforme a entrada cresce pois executa cada entrada por isso ela é O(n) e a função 2 é O(3) independente do valor da entrada.

Assim ao inves de analisar o tempo de execução, apesar de ser importante quando é trabalhado no mesmo hardware uma metrica mais objetiva é usar o Big-O pois damos uma classificação da complexidade. O(n) não é escalavel, quanto mais dados mais tempo vai levar para executar.

---

# Utilizar as Ferramentas Disponíveis

Observe os códigos no arquivo "ponto-2"

---

Funçõs Big-O

- 1       : Constant
- log(n)  : Logarithmic
- n       : Linear
- nlog(n) : Log Linear
- n^2     : Quadratic
- n^3     : Cubic
- 2^n     : Exponential

---

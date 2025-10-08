def collatz_sequence_length(n, cache):
    """
    Calcula o comprimento (número de termos) da sequência de Collatz para um número n.

    A sequência de Collatz é definida assim:
        - Se n for par, o próximo termo é n / 2
        - Se n for ímpar, o próximo termo é 3n + 1
        - A sequência termina quando n = 1

    Este algoritmo utiliza memoização (armazenamento em cache) para evitar
    recalcular sequências que já foram obtidas anteriormente.

    Parâmetros:
    -----------
    n : int
        Número inicial para o cálculo da sequência.
    cache : dict
        Dicionário que armazena os comprimentos de sequências já calculadas.
        A chave é o número e o valor é o comprimento da sequência.

    Retorna:
    --------
    int
        Comprimento total da sequência de Collatz iniciando em n.
    """
    # Verifica se o valor já foi calculado anteriormente
    if n in cache:
        return cache[n]

    # Se n for par, aplica a regra n / 2
    if n % 2 == 0:
        length = 1 + collatz_sequence_length(n // 2, cache)
    # Se n for ímpar, aplica a regra 3n + 1
    else:
        length = 1 + collatz_sequence_length(3 * n + 1, cache)

    # Armazena o resultado no cache para uso futuro
    cache[n] = length
    return length


# Inicializa o cache com o caso base da sequência de Collatz (n = 1)
cache = {1: 1}

# Variáveis para armazenar o maior comprimento encontrado e o número correspondente
longest_chain = 0
number_with_longest = 1

# Loop principal: testa todos os números de 1 até 1 milhão
for n in range(1, 1_000_000):
    # Calcula o comprimento da sequência para o número atual
    length = collatz_sequence_length(n, cache)

    # Atualiza os valores máximos caso uma sequência mais longa seja encontrada
    if length > longest_chain:
        longest_chain = length
        number_with_longest = n

# Exibe o resultado final formatado
print(f"O número com a sequência mais longa é {number_with_longest} com {longest_chain} elementos.")

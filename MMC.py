from functools import reduce

# Função para calcular o Máximo Divisor Comum (MDC)
def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Função para calcular o Mínimo Múltiplo Comum (MMC) entre dois números
def mmc(a, b):
    return (a * b) // mdc(a, b)

# Função para calcular o MMC de uma lista de números
def mmc_de_lista(lista):
    return reduce(mmc, lista)

# Interface de terminal
def main():
    print("=== Calculadora de MMC ===")
    entrada = input("Digite os números separados por espaço: ")

    try:
        numeros = list(map(int, entrada.strip().split()))
        if len(numeros) < 2:
            print("Digite pelo menos dois números.")
            return
        resultado = mmc_de_lista(numeros)
        print(f"O MMC de {numeros} é {resultado}")
    except ValueError:
        print("Entrada inválida. Digite apenas números inteiros separados por espaço.")

# Executa o programa
if __name__ == "__main__":
    main()

def calcular_soma(numeros):
    return sum(numeros)


def calcular_media(numeros):
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)


def encontrar_maior(numeros):
    return max(numeros)


def encontrar_menor(numeros):
    return min(numeros)


def contar_pares(numeros):
    return len([numero for numero in numeros if numero % 2 == 0])


def contar_impares(numeros):
    return len([numero for numero in numeros if numero % 2 != 0])


def exibir_resultado(numeros):
    print("\nResultado da análise:")
    print(f"Números informados: {numeros}")
    print(f"Soma: {calcular_soma(numeros)}")
    print(f"Média: {calcular_media(numeros):.2f}")
    print(f"Maior número: {encontrar_maior(numeros)}")
    print(f"Menor número: {encontrar_menor(numeros)}")
    print(f"Quantidade de números pares: {contar_pares(numeros)}")
    print(f"Quantidade de números ímpares: {contar_impares(numeros)}")


def obter_numeros():
    entrada = input("Digite números inteiros separados por espaço: ")

    try:
        numeros = [int(numero) for numero in entrada.split()]
        return numeros
    except ValueError:
        print("Erro: informe apenas números inteiros.")
        return []


def main():
    print("Analisador de Números em Python")

    numeros = obter_numeros()

    if len(numeros) == 0:
        print("Nenhum número válido foi informado.")
        return

    exibir_resultado(numeros)


if __name__ == "__main__":
    main()
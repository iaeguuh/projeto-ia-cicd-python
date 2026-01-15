def calcular_total_com_desconto(valor, desconto):
    """
    Gerado com o prompt no GitHub Copilot:
    'Crie uma função em Python que calcule o valor final de um pedido aplicando um desconto percentual.'
    """
    if valor < 0 or desconto < 0:
        raise ValueError("Valores inválidos")
    return valor - (valor * desconto / 100)

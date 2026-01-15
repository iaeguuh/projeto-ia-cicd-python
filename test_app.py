from app import calcular_total_com_desconto

def test_calculo_com_desconto():
    """
    Gerado com o prompt no GitHub Copilot:
    'Crie um teste unitário em Python para validar o cálculo de desconto.'
    """
    assert calcular_total_com_desconto(100, 10) == 90

def test_valores_invalidos():
    try:
        calcular_total_com_desconto(-100, 10)
        assert False
    except ValueError:
        assert True

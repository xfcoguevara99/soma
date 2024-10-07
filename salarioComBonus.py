#coding: utf-8

def comissaoSalario():
    nome = input("Entre com o nome do vendedor: ")
    salarioFixo = float(input("Informe o salario do vendedor: "))
    vendas = float(input("infome as vendas realizadas: "))
    comissao = 0.15 * salarioFixo
    pagamentoEsperado = salarioFixo + comissao
    return nome,vendas,pagamentoEsperado

nome,vendas,pagamentoEsperado = comissaoSalario()
strg = "{0} obteve R$ {1:.2f} e vai receber {2:.2f}".format(nome,vendas,pagamentoEsperado)
print(strg)
    
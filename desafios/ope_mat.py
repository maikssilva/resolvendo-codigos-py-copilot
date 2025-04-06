# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

operacao = input("Digite a operação desejada (+, -, *, /): ")
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: Divisão por zero não é permitida."
else:
    resultado = "Erro: Operação inválida."
# Exibindo o resultado da operação
print("Resultado:", resultado)

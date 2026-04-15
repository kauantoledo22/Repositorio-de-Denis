
try:
    a = float(input("Digite o primeiro número (A): "))
    b = float(input("Digite o segundo número (B): "))

    
    if a > b:
        print(f"O número A ({a}) é maior que o número B ({b}).")
    elif b > a:
        print(f"O número B ({b}) é maior que o número A ({a}).")
    else:
        print(f"Os números são iguais: A = {a} e B = {b}.")
except ValueError:
    print("Por favor, digite apenas números válidos.")

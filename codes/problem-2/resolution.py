def FibonacciCalc(number):
    a, b = 0, 1
    while(a < number):
        a, b = b, a+b
        
    if a == number:
        print(f"Number: {number} is a Fibonacci sequence!")
    else:
        print(f"Number: {number} isn't a Fibonacci sequence!")

number = int(input("Choice a number: "))
FibonacciCalc(number)

# Define 'a' = 0 && 'b' = 1;
# Cria um laço de repetição que funciona enquanto 'a' for menor que o número escolhido pelo usuário;
# O laço define o valor de 'b' para 'a' e a soma de 'a'+'b' para 'b';
# Quando o valor de 'a' é igual ou maior que o valor de 'number', o laço acaba e entra na verificação do valor resultante;
# Se o valor resultante de 'a' for igual ao valor de 'number', sabemos que o número escolhido pelo usuário está entre a sequencia de Fibonacci. Mas se não for, sabemos que ele não está na sequencia;
# Depois montramos ao usuário se o número digitado está ou não na sequencia de Fibonacci;

# Temos que observar que não usamos o balor de 'b' para a varificação do 'number', pois 'a' recebe o valor de 'b' e 'b' é usado para armazenar o resultado do próximo valor da operação;
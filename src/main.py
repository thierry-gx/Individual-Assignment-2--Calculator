from random import randint
from random import choice

N = 6
signs = ['+', '-', '*', '/']

def main():
    with open('results.txt', 'w') as fout:
        fout.write("2359280" + '\n')

        for i in range (N):
            numbers = []
            operators = []
            num = randint(3, 5)
            for j in range (num):
                numbers.append(randint(0, 100))
            for j in range (num - 1):
                operators.append(choice(signs))
            result(numbers, operators, fout)
        

def result(numbers, operators, fout):
    expression = str(numbers[0])
    for num, op in zip(numbers[1:], operators):
        expression += f'{op}{num}'
    print(expression, end = "")
    res = eval(expression)
    if isinstance(res, int):
       output = f"={res}"
    else:
        output = f"={res:.2f}"
    
    print(output)
    fout.write(output + '\n')

main()

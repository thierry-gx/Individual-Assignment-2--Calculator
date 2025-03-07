from random import randint
from random import choice

N = 6
signs = ['+', '-', '*', '/']

def main():
    for i in range (N):
        numbers = []
        operators = []
        num = randint(3, 5)
        for j in range (num):
            numbers.append(randint(0, 100))
        for j in range (num - 1):
            operators.append(choice(signs))
        result(numbers, operators)
        

def result(numbers, operators):
    expression = str(numbers[0])
    for num, op in zip(numbers[1:], operators):
        expression += f'{op}{num}'
    print(expression, end = "")
    res = eval(expression)
    if isinstance(res, int):
        print(f"={res}")
    else:
        print(f"={res:.2f}")

main()

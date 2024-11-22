import random

class Coder:
    def __init__(self, numbers):
        self.numbers = list(map(int, numbers.split()))
        self.result = self.coder()

    def coder(self):
        operation = random.choice(["+", "-", "*", "/"])
        if operation == '+':
            return sum(self.numbers)
        elif operation == '-':
            result = self.numbers[0]
            for num in self.numbers[1:]:
                result -= num
            return result
        elif operation == '*':
            result = 1
            for num in self.numbers:
                result *= num
            return result
        elif operation == '/':
            result = self.numbers[0]
            for num in self.numbers[1:]:
                if num != 0:
                    result /= num
                else:
                    result = 'You can\'t divide by 0'
                    break
            return result

    def __repr__(self):
        return str(self.result)

def check():
    while True:
        numbers = input("Print your numbers: ")
        try:
            list(map(int, numbers.split()))
            return numbers
        except ValueError:
            print("You can write only numbers")

numbers = check()
reslt = Coder(numbers)
print(reslt)

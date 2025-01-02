import math

class TaylorFunctions:
    @staticmethod
    def factorial(n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    @staticmethod
    def sin(x, terms=15):
        x = x % (2 * math.pi)  # Приведение x к диапазону [0, 2*pi]
        if x > math.pi:        # Приведение к диапазону [-pi, pi]
            x -= 2 * math.pi
        result = 0
        for n in range(terms):
            sign = (-1) ** n
            term = sign * (x ** (2 * n + 1)) / TaylorFunctions.factorial(2 * n + 1)
            result += term
        return result

    @staticmethod
    def cos(x, terms=15):
        x = x % (2 * math.pi)  # Приведение x к диапазону [0, 2*pi]
        if x > math.pi:        # Приведение к диапазону [-pi, pi]
            x -= 2 * math.pi
        result = 0
        for n in range(terms):
            sign = (-1) ** n
            term = sign * (x ** (2 * n)) / TaylorFunctions.factorial(2 * n)
            result += term
        return result

    @staticmethod
    def ln(x, terms=50):
        if x <= 0:
            raise ValueError("Логарифм не определен для неположительных значений.")
        if x == 1:
            return 0
        if x > 1:
            return TaylorFunctions.ln(x / 2.71828, terms) + 1
        result = 0
        for n in range(1, terms + 1):
            term = ((-1) ** (n + 1)) * ((x - 1) ** n) / n
            result += term
        return result




from taylor_functions import TaylorFunctions

class MainFunction:
    @staticmethod
    def f(x):
        if x >= 0:
            ln_x = TaylorFunctions.ln(x + 1e-10)  # Избежание деления на 0
            cos_x = TaylorFunctions.cos(x)
            return ln_x * cos_x
        else:
            sin_x = abs(TaylorFunctions.sin(x))
            cos_x = TaylorFunctions.cos(x)
            ln_abs_x = TaylorFunctions.ln(abs(x) + 1e-10)  # Избежание деления на 0
            denominator = ln_abs_x + 1
            if denominator == 0:
                raise ZeroDivisionError("Denominator in function is zero")
            return (sin_x - cos_x) / denominator

class Formulas():
    def __init__(self, x):
        self.x = x

    def calculation_1(self):
        try:
            if self.x <= 1.707 or self.x >= 106.33:
                return self.x**4 * 4.968 + self.x**3 * 2.271 - self.x**2 * 3.589 + self.x * 3.317
        except TypeError:
            return "Error"

    def calculation_2(self):
        try:
            if self.x <= 1.707 or self.x >= 106.33:
                return self.x**3 * 3.774 - self.x**2 * 2.298 + self.x * 3.873
        except TypeError:
            return "Error"

    def calculation_3(self):
        try:
            if self.x <= 1.707 or self.x >= 106.33:
                return self.x**2 * 4.165 + self.x * 3.363
        except TypeError:
            return "Error"

    def calculation_4(self):
        try:
            if self.x <= 1.707 or self.x >= 106.33:
                return self.x*6.363
        except TypeError:
            return "Error"

if __name__ == '__main__':
    F = Formulas(300)
    print(F.calculation_1(), F.calculation_2(), F.calculation_3(), F.calculation_4())
class Polynomial_Multiplier:
    def __init__(self, poly_1, poly_2, variable='x'):
        self.poly_1 = poly_1
        self.poly_2 = poly_2
        self.variable = variable
        self.result_coefficients = [0] * (len(self.poly_1) + len(self.poly_2) - 1)
        self.result_terms = []

    def multiply(self):
        for i in range(len(self.poly_1)):
            for j in range(len(self.poly_2)):
                self.result_coefficients[i + j] += self.poly_1[i] * self.poly_2[j]
        return self

    def print_result(self):
        for i in range(len(self.result_coefficients)):
            if self.result_coefficients[i] != 0:
                degree = len(self.result_coefficients) - i - 1
                if degree == 0:
                    self.result_terms.append(str(self.result_coefficients[i]))
                elif degree == 1:
                    self.result_terms.append(f"{self.result_coefficients[i]}{self.variable}")
                else:
                    self.result_terms.append(f"{self.result_coefficients[i]}{self.variable}^{degree}")
        print(" + ".join(self.result_terms))


Polynomial_Multiplier([3, 2], [3, 0, 4, 0, 5]).multiply().print_result()

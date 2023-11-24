class Polynomial_Multiplier:
    def __init__(self, poly_1, poly_2, variable="x"):
        self.poly_1 = poly_1
        self.poly_2 = poly_2
        self.poly_1_len = len(self.poly_1)
        self.poly_2_len = len(self.poly_2)
        self.variable = variable
        self.expanded_product_list = [0] * (self.poly_1_len + self.poly_2_len - 1)
        self.formatted_result_terms = []

    def multiply(self):
        for i in range(self.poly_1_len):
            for j in range(self.poly_2_len):
                self.expanded_product_list[i + j] += self.poly_1[i] * self.poly_2[j]
        return self

    def print_result(self):
        result_len = len(self.expanded_product_list)
        for i in range(result_len):
            if self.expanded_product_list[i] != 0:
                degree = result_len - i - 1
                if degree == 0:
                    self.formatted_result_terms.append(
                        str(self.expanded_product_list[i])
                    )
                elif degree == 1:
                    self.formatted_result_terms.append(
                        f"{self.expanded_product_list[i]}{self.variable}"
                    )
                else:
                    self.formatted_result_terms.append(
                        f"{self.expanded_product_list[i]}{self.variable}^{degree}"
                    )
        print(" + ".join(self.formatted_result_terms))


Polynomial_Multiplier([3, 2], [3, 0, 4, 0, 5]).multiply().print_result()

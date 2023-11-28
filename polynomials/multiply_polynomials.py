class Polynomial_Multiplier:
    """
    A class that represents a polynomial multiplier.

    Attributes:
        poly_1 (list): The coefficients of the first polynomial.
        poly_2 (list): The coefficients of the second polynomial.
        variable (str): The variable symbol used in the polynomial expression.
        expanded_product_list (list): The coefficients of the expanded product of the two polynomials.

    Methods:
        multiply: Multiplies the two polynomials and updates the expanded product list.
        print_result: Prints the result polynomial in a formatted way.
    """

    def __init__(self, poly_1, poly_2, variable="x"):
        self.poly_1 = poly_1
        self.poly_2 = poly_2
        self.poly_1_degree = len(self.poly_1) - 1
        self.poly_2_degree = len(self.poly_2) - 1
        self.variable = variable
        self.product = [0] * (self.poly_1_degree + self.poly_2_degree + 1)

    def multiply(self):
        """
        Multiplies the two polynomials and updates the expanded product list.

        Returns:
            Polynomial_Multiplier: The current instance of the Polynomial_Multiplier class.
        """
        for i in range(self.poly_1_degree + 1):
            for j in range(self.poly_2_degree + 1):
                self.product[i + j] += self.poly_1[i] * self.poly_2[j]
        return self

    def print_result(self):
        """
        Prints the result polynomial in a formatted way.
        """
        formatted_expanded_product = []
        result_len = len(self.product)
        for i in range(result_len):
            if self.product[i] != 0:
                degree = result_len - i - 1
                if degree == 0:
                    formatted_expanded_product.append(
                        str(self.product[i])
                    )
                elif degree == 1:
                    formatted_expanded_product.append(
                        f"{self.product[i]}{self.variable}"
                    )
                else:
                    formatted_expanded_product.append(
                        f"{self.product[i]}{self.variable}^{degree}"
                    )
        print(" + ".join(formatted_expanded_product))


Polynomial_Multiplier([1, 3], [2, -5, 8]).multiply().print_result()

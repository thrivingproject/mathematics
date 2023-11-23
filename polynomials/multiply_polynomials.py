poly1 = [1, 9]
poly2 = [1, 2, 0]
variable = "x"


def multiply_polynomials(poly1, poly2, variable="x"):
    # Initialize the result polynomial (using list replication)
    result = [0] * (len(poly1) + len(poly2) - 1)

    # Multiply each term of the first polynomial
    # with each term of the second polynomial
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            result[i + j] += poly1[i] * poly2[j]

    # Convert to string
    terms = []
    for i in range(len(result)):
        if result[i] != 0:
            # Get the degree of the term
            degree = len(result) - i - 1
            # Format the term
            if degree == 0:
                terms.append(str(result[i]))
            elif degree == 1:
                terms.append(f"{result[i]}{variable}")
            else:
                terms.append(f"{result[i]}{variable}^{degree}")
    return " + ".join(terms)


print("Resultant Polynomial: ", multiply_polynomials(poly1, poly2, variable))

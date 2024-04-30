class Polynomial:

    def __init__(self, *coefficients):
        if len(coefficients) == 1 and isinstance(coefficients[0], dict):
            self.coefficients = coefficients[0]
        elif len(coefficients) == 1 and isinstance(coefficients[0], list):
            self.coefficients = {i: coefficients[0][i] for i in range(len(coefficients[0]))}
        else:
            self.coefficients = {i: coefficients[i] for i in range(len(coefficients))}

    def __repr__(self):
        pass

    def __str__(self):
        result = ""
        for degree in sorted(self.coefficients.keys(), reverse=True):
            coeff = self.coefficients[degree]
            if coeff != 0:
                if degree == 0:
                    result += f"{coeff}"
                elif degree == 1:
                    result += f"{coeff}x + "
                else:
                    result += f"{coeff}x^{degree} + "

        return result.rstrip(" + ")

    def __eq__(self, other):
        pass

    def __add__(self, other):
        result_poly = []
        if isinstance(other, Polynomial):
            for i in range(max(len(self.coefficients), len(other.coefficients))):
                if i < len(self.coefficients):
                    term1 = self.coefficients[i]
                else:
                    term1 = 0
                if i < len(other.coefficients):
                    term2 = other.coefficients[i]
                else:
                    term2 = 0
                result_poly.append(term1 + term2)
        else:
            poly = Polynomial(other)
            for i in range(max(len(self.coefficients), len(poly.coefficients))):
                if i < len(self.coefficients):
                    term1 = self.coefficients[i]
                else:
                    term1 = 0
                if i < len(poly.coefficients):
                    term2 = poly.coefficients[i]
                else:
                    term2 = 0
                result_poly.append(term1 + term2)
        return Polynomial(*result_poly)


    def __radd__(self, other):
        pass

    def __neg__(self):
        pass

    def __sub__(self, other):
        result_poly = []
        if isinstance(other, Polynomial):
            for i in range(max(len(self.coefficients), len(other.coefficients))):
                if i < len(self.coefficients):
                    term1 = self.coefficients[i]
                else:
                    term1 = 0
                if i < len(other.coefficients):
                    term2 = other.coefficients[i]
                else:
                    term2 = 0
                result_poly.append(term1 - term2)
        else:
            poly = Polynomial(other)
            for i in range(max(len(self.coefficients), len(poly.coefficients))):
                if i < len(self.coefficients):
                    term1 = self.coefficients[i]
                else:
                    term1 = 0
                if i < len(poly.coefficients):
                    term2 = poly.coefficients[i]
                else:
                    term2 = 0
                result_poly.append(term1 - term2)
        return Polynomial(*result_poly)

    def __rsub__(self, other):
        pass

    def __call__(self, x):
        pass

    def degree(self):
        pass

    def der(self, d=1):
        pass

    def __mul__(self, other):
        pass

    def __rmul__(self, other):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass

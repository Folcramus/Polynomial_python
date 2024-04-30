class Polynomial:

    def __init__(self, *coefficients):
        if len(coefficients) == 1 and isinstance(coefficients[0], dict):
            self.coefficients = coefficients[0]
        elif len(coefficients) == 1 and isinstance(coefficients[0], list):
            self.coefficients = {i: coefficients[0][i] for i in range(len(coefficients[0]))}
        else:
            self.coefficients = {i: coefficients[i] for i in range(len(coefficients))}

    def __repr__(self):
        res = str(self.coefficients.values()).replace("dict_values(", "")
        res = str(res.replace(")", ""))
        return f'Polynomial {res}'

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
        enum = None
        result_poly = {}
        if isinstance(other, Polynomial) is False:
            other = Polynomial(other)
            if len(self.coefficients) >= len(other.coefficients):
                enum = self
            elif len(self.coefficients) < len(other.coefficients):
                enum = other
        index = 0
        for i in enum.coefficients:

            if index < len(self.coefficients):
                term1 = self.coefficients[i]
            else:
                term1 = 0
            if index < len(other.coefficients):
                term2 = other.coefficients[i]
            else:
                term2 = 0
            index += 1
            result_poly.update({i: term1 + term2})

        return Polynomial(result_poly)


    def __radd__(self, other):
        enum = None
        result_poly = {}
        if isinstance(other, Polynomial) is False:
            other = Polynomial(other)
            if len(self.coefficients) >= len(other.coefficients):
                enum = self
            elif len(self.coefficients) < len(other.coefficients):
                enum = other
        index = 0
        for i in enum.coefficients:

            if index < len(self.coefficients):
                term1 = self.coefficients[i]
            else:
                term1 = 0
            if index < len(other.coefficients):
                term2 = other.coefficients[i]
            else:
                term2 = 0
            index += 1
            result_poly.update({i: term1 + term2})

        return Polynomial(result_poly)


    def __neg__(self):
        pass

    def __sub__(self, other):
        enum = None
        result_poly = {}
        if isinstance(other, Polynomial) is False:
            other = Polynomial(other)
            if len(self.coefficients) >= len(other.coefficients):
                enum = self
            elif len(self.coefficients) < len(other.coefficients):
                enum = other
        index = 0
        for i in enum.coefficients:

            if index < len(self.coefficients):
                term1 = self.coefficients[i]
            else:
                term1 = 0
            if index < len(other.coefficients):
                term2 = other.coefficients[i]
            else:
                term2 = 0
            index+=1
            result_poly.update({i: term1 - term2})

        return Polynomial(result_poly)

    def __rsub__(self, other):
        enum = None
        result_poly = {}
        if isinstance(other, Polynomial) is False:
            other = Polynomial(other)
            if len(self.coefficients) >= len(other.coefficients):
                enum = self
            elif len(self.coefficients) < len(other.coefficients):
                enum = other
        index = 0
        for i in enum.coefficients:

            if index < len(self.coefficients):
                term1 = self.coefficients[i]
            else:
                term1 = 0
            if index < len(other.coefficients):
                term2 = other.coefficients[i]
            else:
                term2 = 0
            index += 1
            result_poly.update({i: term2 - term1})

        return Polynomial(result_poly)

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
        return self.coefficients.items().__iter__()

    def __next__(self):
        return next(self.coefficients.items().__iter__())

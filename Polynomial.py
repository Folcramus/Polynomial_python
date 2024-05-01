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
                    if coeff > 0:
                        result += f" + {coeff}"
                    elif coeff < 0:
                        result += f" - {-coeff}"
                elif degree == 1:
                    if coeff > 0:
                        result += f" + {coeff}x"
                    elif coeff < 0:
                        result += f" - {-coeff}x"
                else:
                    if coeff > 0:
                        result += f" + {coeff}x^{degree}"
                    elif coeff < 0:
                        result += f" - {-coeff}x^{degree}"
        return result.lstrip(' +')

    def __eq__(self, other):
        if len(self.coefficients) != len(other.coefficients):
            return False

        for key in self.coefficients.keys():
            if key not in other.coefficients or self.coefficients[key] != other.coefficients[key]:
                return False

        return True

    def __add__(self, other):
        enum = None
        result_poly = {}
        if isinstance(other, Polynomial) is False:
            other = Polynomial(other)
        if len(self.coefficients) >= len(other.coefficients):
            enum = self
        elif len(self.coefficients) < len(other.coefficients):
            enum = other
        elif len(self.coefficients) == len(other.coefficients):
            enum = self
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
        for k, i in self.coefficients.items():
            self.coefficients[k] = -self.coefficients[k]
        return self

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
            index += 1
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
        result = 0
        for power, coeff in self.coefficients.items():
            result += coeff * (x ** power)
        return result

    def degree(self):
        return max(self.coefficients.keys())

    def der(self, d=1):
        res = self.coefficients
        while d != 0 and d > 0:
            temp = {}
            for k, i in res.items():
                if i != 0:
                    temp.update({k - 1: k * i})
            d -= 1
            res = temp
        return Polynomial(res)

    def __mul__(self, other):
        res = {}

        for deg1, coeff1 in self.coefficients.items():
            for deg2, coeff2 in other.coefficients.items():
                new_deg = deg1 + deg2
                new_coeff = coeff1 * coeff2

                if new_deg in res:
                    res[new_deg] += new_coeff
                else:
                    res[new_deg] = new_coeff
        return Polynomial(res)

    def __rmul__(self, other):
        res = {}

        for deg1, coeff1 in self.coefficients.items():
            for deg2, coeff2 in other.coefficients.items():
                new_deg = deg1 + deg2
                new_coeff = coeff1 * coeff2

                if new_deg in res:
                    res[new_deg] += new_coeff
                else:
                    res[new_deg] = new_coeff
        return Polynomial(res)

    def __iter__(self):
        return self.coefficients.items().__iter__()

    def __next__(self):
        return next(self.coefficients.items().__iter__())

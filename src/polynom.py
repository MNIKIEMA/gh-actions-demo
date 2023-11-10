"""
Polynom class for polynomials of degree 1 or higher.
"""


class Polynomial:
    
    def __init__(self, *coefs):
        self.coefs = list(coefs)
        self.degre = len(coefs)-1

    def __repr__(self) -> str:
        def x_expr(degree):
            if degree == 0:
                res = ""
            elif degree == 1:
                res = "X"
            else:
                res = "X^"+str(degree)
            return res

        degree = len(self.coefs) - 1
        res = ""

        for i in range(0, degree+1):
            coeff = self.coefs[i]
            # nothing has to be done if coeff is 0:
            if abs(coeff) == 1 and i < degree:
                # 1 in front of x shouldn't occur, e.g. x instead of 1x
                # but we need the plus or minus sign:
                res += f"{'+' if coeff>0 else '-'}{x_expr(degree-i)}" 
                res += " " 
            elif coeff != 0:
                res += f"{coeff:+g}{x_expr(degree-i)}" 
                res += " "
        return res.lstrip('+')
        
    def __call__(self, x):
        res = 0
        for index, coeff in enumerate(self.coefs[::-1]):
            res += coeff * x** index
        return res
    

    def __eq__(self, other: object) -> bool:
        return other.degre == self.degre and other.coefs ==self.coefs
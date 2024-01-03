# 最大公约数:欧几里得算法
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def gcd2(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a


# 约分
class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        x = self.gcd(a, b)
        self.a /= x
        self.b /= x

    def gcd(self, a, b):
        while b > 0:
            r = a % b
            a = b
            b = r
        return a

    def ags(self, a, b):
        r = gcd(a, b)
        return a * b / r

    def __add__(self, other):
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        denominator = self.ags(b, d)
        numerator = a * (denominator / b) + c * (denominator / d)
        return Fraction(numerator, denominator)

    def __str__(self):
        return '%d/%d' % (self.a, self.b)


print(gcd(12, 16))
print(gcd2(12, 16))
a = Fraction(1, 6)
b = Fraction(1, 2)
print(a + b)

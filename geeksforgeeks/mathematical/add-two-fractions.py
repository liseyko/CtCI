def addFraction(num1, den1, num2, den2):
    num = num1 * den2 + num2 * den1
    den = den1 * den2
    gcd, div = num, den
    while div:
        gcd, div = div, gcd % div

    print('%s/%s'% (num // gcd, den // gcd))

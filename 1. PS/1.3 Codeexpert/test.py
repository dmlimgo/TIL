import decimal

D = decimal.Decimal
max = D('41443.39354110')
print(max)
print(max.quantize(D('0.001'), rounding=decimal.ROUND_HALF_UP))



x=D('32.50')*D('0.19')
print(x)
print(x.quantize(D('0.01'),rounding=decimal.ROUND_HALF_UP))


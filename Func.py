def print_func():
    print('A')
    print('B')
    print('C')

def vat_calc(price, vat_rate = 0.1):
    return price * vat_rate


print(vat_calc(1000))
print(vat_calc(10000, 0.2))
print(vat_calc(100000, 0.3))

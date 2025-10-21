amount = 0
for p in range(int(input())):
    product, q = map(int, input().split())
    product = product - 1000
    amount += (product + 0.5) * q
print('%0.2f' % amount)
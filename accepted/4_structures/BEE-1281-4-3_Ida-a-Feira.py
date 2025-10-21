N = int(input())
for trip in range(N):
    products = {}
    
    M = int(input())
    for product in range(M):
        product = input().split()
        products[product[0]] = float(product[1])

    price = 0
    P = int(input())
    for product in range(P):
        product = input().split()
        price += products[product[0]] * int(product[1])

    print("R$ {:.2f}".format(round(price, ndigits=2)))
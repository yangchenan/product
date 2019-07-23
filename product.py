product = []
while True:
	name = input('商品名稱:')
	if name == 'q':
		break
	price = input('價格:')
	product.append([name, price])
print(product)

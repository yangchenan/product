product = []
while True:
	name = input('商品名稱:')
	if name == 'q':
		break
	price = input('價格:')
	product.append([name, price])
print(product)

total = 0
for p in product:
	print(p[1])
	total = total + int(p[1])
print(total)
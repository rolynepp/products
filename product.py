products =[]
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q': #quit
		break
	price = input('請輸入價格: ')
	price = int(price)
	#p = []
	#p.append(name)
	#p.append(price) 下方為清單簡化
	p = [name, price]
	products.append(p)
print(products)

for p in products:
	print(p[0], '的價格是', p[1])

with open('products.txt', 'w') as f:
	for p in products:
		f.write(p[0] + ','+ str(p[1]) + '\n')
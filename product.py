product =[]
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q': #quit
		break
	price = input('請輸入價格: ')
	p = []
	p.append(name)
	p.append(price)
	product.append(p)
print(product)
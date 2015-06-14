import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oxfam_project.settings')

import django
django.setup()

from manager.models import Shop, Commodity

def populate():
	glasgow_shop = add_shop(name="Glasgow Shop", email="gla@gla.gla", address="Glasgow")
	add_commodity(name="g_Book", shop=glasgow_shop, price=10.04, comments="Good book")
	add_commodity(name="g_Shirt", shop=glasgow_shop, price=19.99, comments="Cool Shirt")
	add_commodity(name="g_Cable", shop=glasgow_shop, price=8.64, comments="Useful cable")
	add_commodity(name="g_Cookie", shop=glasgow_shop, price=1.04, comments="Tasty cookie")
	add_commodity(name="g_Fruit", shop=glasgow_shop, price=0.74, comments="Epic apple")
	add_commodity(name="g_Cup", shop=glasgow_shop, price=1.04, comments="Nice cup")
	add_commodity(name="g_Spoon", shop=glasgow_shop, price=0.74, comments="Useful spoon")
	add_commodity(name="g_Soap", shop=glasgow_shop, price=1.04, comments="Nice soap")
	add_commodity(name="g_Fork", shop=glasgow_shop, price=0.74, comments="Good fork")

	edinburgh_shop = add_shop(name="Edinburgh Shop", email="edi@edi.edi", address="Edinburgh")
	add_commodity(name="e_Book", shop=edinburgh_shop, price=10.04, comments="Good book")
	add_commodity(name="e_Shirt", shop=edinburgh_shop, price=19.99, comments="Cool Shirt")
	add_commodity(name="e_Cable", shop=edinburgh_shop, price=8.64, comments="Useful cable")
	add_commodity(name="e_Cookie", shop=edinburgh_shop, price=1.04, comments="Tasty cookie")
	add_commodity(name="e_Fruit", shop=edinburgh_shop, price=0.74, comments="Epic apple")
	add_commodity(name="e_Cup", shop=edinburgh_shop, price=1.04, comments="Nice cup")
	add_commodity(name="e_Spoon", shop=edinburgh_shop, price=0.74, comments="Useful spoon")
	add_commodity(name="e_Soap", shop=edinburgh_shop, price=1.04, comments="Nice soap")
	add_commodity(name="e_Fork", shop=edinburgh_shop, price=0.74, comments="Good fork")

	aberdeen_shop = add_shop(name="Aberdeen Shop", email="abe@abe.abe", address="Aberdeen")
	add_commodity(name="a_Book", shop=aberdeen_shop, price=10.04, comments="Good book")
	add_commodity(name="a_Shirt", shop=aberdeen_shop, price=19.99, comments="Cool Shirt")
	add_commodity(name="a_Cable", shop=aberdeen_shop, price=8.64, comments="Useful cable")
	add_commodity(name="a_Cookie", shop=aberdeen_shop, price=1.04, comments="Tasty cookie")
	add_commodity(name="a_Fruit", shop=aberdeen_shop, price=0.74, comments="Epic apple")
	add_commodity(name="a_Cup", shop=aberdeen_shop, price=1.04, comments="Nice cup")
	add_commodity(name="a_Spoon", shop=aberdeen_shop, price=0.74, comments="Useful spoon")
	add_commodity(name="a_Soap", shop=aberdeen_shop, price=1.04, comments="Nice soap")
	add_commodity(name="a_Fork", shop=aberdeen_shop, price=0.74, comments="Good fork")

	for shop in Shop.objects.all():
		for commodity in Commodity.objects.filter(shop=shop):
			print "- {0} - {1}".format(str(shop), str(commodity))

def add_shop(name, email, address):
	shop = Shop.objects.get_or_create(
		name=name,
		email=email,
		address=address)[0]

	return shop


def add_commodity(name, shop, price, comments):
	commodity = Commodity.objects.get_or_create(
		name=name,
		shop=shop,
		price=price,
		comments=comments)[0]

	return shop

if __name__ == '__main__':
	print "Starting manager population script..."
	populate()

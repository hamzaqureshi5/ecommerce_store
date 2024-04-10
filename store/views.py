from django.shortcuts import render
from . models import *
# from . utils import cookieCart, cartData, guestOrder

# Create your views here.


def store(request):
	products = Product.objects.all()
	context = {'products':products}
	return render(request, 'store/store.html', context)


def cart(request):
#	if request.user.is_authenticated():
	customer = request.user.customer
	order, created = Order.objects.get_or_create(customer=customer, complete= False)
	items = order.orderitem_set.all()
#	else:
#		items= []
	order ={"get_cart_item":0, "get_cart_total":1}
	cartItems = {}
	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/cart.html', context)

def checkout(request):
#	if request.user.is_authenticated():
	customer = request.user.customer
	order, created = Order.objects.get_or_create(customer=customer, complete= False)
	items = order.orderitem_set.all()
#	else:
#		items= []
	order ={"get_cart_item":5, "get_cart_total":999.99}
	cartItems = {}
	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/checkout.html', context)

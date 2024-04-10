from django.shortcuts import render
from django.http import JsonResponse
from . models import *
import json
# from . utils import cookieCart, cartData, guestOrder

# Create your views here.


def store(request):
#	if request.user.is_authenticated():
	customer = request.user.customer
	order, created = Order.objects.get_or_create(customer=customer, complete= False)
	items = order.orderitem_set.all()
	cartitems = order.get_cart_items
#	else:
#		items=[]
#		order = {}
#		cartitems = order['get_cart_items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartitems}
	return render(request, 'store/store.html', context)


def cart(request):
#	if request.user.is_authenticated():
	customer = request.user.customer
	order, created = Order.objects.get_or_create(customer=customer, complete= False)
	items = order.orderitem_set.all()
	cartitems = order.get_cart_items

#	else:
#		items= []
#	order ={"get_cart_item":0, "get_cart_total":1}
#	cartItems = {}
	context = {'items':items, 'order':order, 'cartItems':cartitems}
	return render(request, 'store/cart.html', context)

def checkout(request):
#	if request.user.is_authenticated():
	customer = request.user.customer
	order, created = Order.objects.get_or_create(customer=customer, complete= False)
	items = order.orderitem_set.all()
	cartitems = order.get_cart_items
#	else:
#		items= []
#	order ={"get_cart_item":5, "get_cart_total":999.99}
#	cartItems = {}
	context = {'items':items, 'order':order, 'cartItems':cartitems}
	return render(request, 'store/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

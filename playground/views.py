from django.db.models import Q, F, Value, Func, ExpressionWrapper
from django.db.models.aggregates import Count, Max, Min, Sum
from django.db.models.functions import Concat
from django.db import transaction
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, OrderItem, Order, Promotion, Collection, Cart, CartItem, Customer, Address
from tags.models import TaggedItem


def say_hello(request):
    queryset = Product.objects.all()
    list(queryset)
    list(queryset)
    return render(request, 'hello.html', {'name': "Alex", 'tags': list(queryset)})

# вопрос - КАК ОТОБРАЗИТЬ ЭТО В TEMPLATES?????
# product_l = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]

#product_l = Product.objects.filter(inventory__lt=10, unit_price__lt=20)
# #product_l = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)
# WHERE ("store_product"."inventory" < 10 AND "store_product"."unit_price" < 20)

# product = Product.objects.filter(pk=0).first()

# queryset = TaggedItem.objects.get_tags_for(Product, 1)
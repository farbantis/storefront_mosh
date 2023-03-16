from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status


@api_view(['GET', 'POST'])  # перечень доступных к обработке методов
def product_list(request):
    if request.method == 'GET':
        # !!! если не включим collection, в сериалайзере будет млн запросов...
        queryset = Product.objects.select_related('collection').all()
        # в сериалайзер можно отправить объек или квери сэт
        serializer = ProductSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        # десериализируем data=request.data
        serializer = ProductSerializer(data=request.data)
        # данные будут доступны в  serializer.validated_data
        serializer.is_valid(raise_exception=True)  # автоматом вернет ответ 400
        # django добавил туда еще collection
        # print(serializer.validated_data) - если есть save, уже не нужен
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # этот код длиннее чет тот, что выше
        # if serializer.is_valid():
        #     serializer.validated_data
        #     return Response('ok')
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, id):
    # product = Product.objects.get(pk=id)
    product = get_object_or_404(Product, pk=id)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        if product.orderitem_set.count() > 0:
            return Response({'error', 'product cant be deleted as it is associated with an order item'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view()
def collection_detail(request, pk):
    return Response('ok')

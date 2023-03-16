from rest_framework import serializers
from .models import Product, Collection
from decimal import Decimal


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title']


# model serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # by defauld collection represented by ID  '__all__' так делать не нужно
        fields = ['id', 'title', 'description', 'slug', 'inventory', 'unit_price', 'price_with_tax', 'collection']

    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)

    # переопределяем create method, если нужно записать другие данные
    # def create(self, validated_data):
    #     product = Product(**validated_data)
    #     product.other = 1
    #     product.save()
    #     return product

    # переопределяем update
    # def update(self, instance, validated_data):
    #     instance.unit_price = validated_data.get('unit_price')
    #     instance.save()
    #     return instance

    # переопределяем метод валидации... если к примеру нам нужно сравнить пароли...
    # def validate(self, data):
    #     if data['password'] != data['confirm_password']:
    #         return serializers.ValidationError('passwords dont match')
    #     return data


    # collection = serializers.HyperlinkedRelatedField(
    #     queryset=Collection.objects.all(),
    #     view_name='collection-detail'
    # )

# www.django-rest-framework.org -- документация
# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
#     # если мы поле называем по другому, не unit_price, а price
#     # price = serializers.DecimalField(max_digits=6, decimal_places=2, source='unit_price')
#     unit_price = serializers.DecimalField(max_digits=6, decimal_places=2)
#     # добавим поле, которого нет в модели
#     price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
#     # связываем две модели 2 варианта
#     # 1) получим ID
#     # collection = serializers.PrimaryKeyRelatedField(
#     #     queryset=Collection.objects.all()
#     # )
#     # 2) получим строку... конвертирует каждую коллекцию в строку
#     # collection = serializers.StringRelatedField()
#     # 3) сделать сериалайзер для Collection !!! теперь возвращает и ID, title !!!!
#     # collection = CollectionSerializer()
#     # 4) а можно и так... теперь возвращает URL адрес !!!!
#     collection = serializers.HyperlinkedRelatedField(
#         queryset=Collection.objects.all(),
#         view_name='collection-detail'
#     )




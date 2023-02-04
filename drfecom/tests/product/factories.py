import factory

from drfecom.product.models import Category,Brand,Product

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = 'test_category'

class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand
    
    name = 'test_brand'

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
    
    name = 'test_product'
    is_digital = True
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)
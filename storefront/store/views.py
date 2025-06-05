from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product, OrderItem , Order, Customer, Collection
from django.db.models import Q, F, Func
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.db.models import Value, Count
from django.db.models.functions import Concat 
from django.db.models import ExpressionWrapper, DecimalField
from django.contrib.contenttypes.models import  ContentType



def fetch(request): 
    query_set=Product.objects.all()
    # TaggedItem.objects.get_tags_for(Product, 1)
    # query_set = Product.objects.filter(unit_price__range=(20, 30))  
    # query_set = Product.objects.filter(title__icontains='coffee')
    # Products: inventory < 10 AND price < 20

    # query_set = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)
    # query_set = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    #Products: inventory = price
    # query_set = Product.objects.filter(inventory=F('collection__id'))
    #Sorting Data
    #012345
    #56789
    # query_set = Product.objects.all()[5:10]
    #return id and title so we use values
    #Getting bunch of tuples insted of dictionaries #values_list
    # query_set = Product.objects.values_list('id','title', 'collection__title')
    
    # query_set = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
    #Deferrig Fields
    # query_set = Product.objects.only('id', 'title')
    # query_set = Product.objects.defer('description')
    #Selecting Related objects
    # query_set = Product.objects.prefetch_related('promotions').select_related('collection').all()
    # query_set = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    #Select_related (1)
    # prefetch_related (n)
    #Select_related method django creates join between tables
    # To get rid of duplicates we can use distinct methods

    # exists = Product.objects.filter(pk=0).exists()
    # query_set.filter().filter.order_by()
    # Max or Average price of out products
    # result = Product.objects.filter(collection__id=1).aggregate(
    #     count=Count('id'), min_price=Min('unit_price'))

    #Annotating Objects
    # query_set = Customer.objects.annotate(is_new=Value(True)) 
    # query_set = Customer.objects.annotate(new_id=F('id') + 1) 
    # query_set = Customer.objects.annotate(
    #     #CONCATE
    #     full_name=Func(F('first_name'), Value(' ') , F('last_name'), function='CONCAT')
    # )
    # query_set = Customer.objects.annotate(
    #     #CONCATE
    #     full_name=Conc   at('first_name', Value(' '), 'last_name')
    # )
        # orders_count = Count('order')
    # discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    # query_set = Product.objects.annotate(discounted_price = discounted_price)
    # content_type = ContentType.objects.get_for_model(Product)

    # query_set = TaggedItem.objects.select_related('tag').filter(
    #     content_type=content_type, 
    #     object_id=1
    # )
    # # Cache
    # query_set = Product.objects.all()
    # query_set[0]
    # list(query_set)
    # collection = Collection.objects.get(pk=11)
    
    # collection.feature_product = None 
    # collection.save()
    # collection.feature_product_id = 1
    # Collection.objects.filter(pk=11).update(featured_product=None)
    # collection = Collection(pk=11)
    # collection.delete()
    # collection.objects.filter(id__gt=5).delete() 

    return render(request, 'hello.html', {'name' : 'NAVEEN REDDY', 'result': list(query_set)})
# Create your views here.
# Takes request and returns response
# request handller

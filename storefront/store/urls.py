from django.urls import path
from store.views import product_list, product_detail, collection_list, collection_detail

urlpatterns = [
    path('product_list/', product_list, name='product_list'),
    path('product_detail/<int:id>/', product_detail, name='product_detail'),
    path('collection_list/', collection_list, name='collection_list'),
    path('collection_detail/<int:pk>/', collection_detail, name='collection_detail'),
]





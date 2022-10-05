from django.contrib import admin
from django.urls import path
from lab1_1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.GetOrders),
    path('order/<int:id>/', views.GetOrder, name='order_url'),
]




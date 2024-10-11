from django.urls import path
from . import views

urlpatterns = [
    path('', views.your_orders, name="your_orders"),
    path('order/', views.order_chai, name='order'),
    path('<int:pk>/edit/', views.edit_chai, name='edit_chai'),
    path('<int:pk>/delete', views.delete_chai, name='delete_chai'),
    
]

"""OnlineStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Store.views import new_order_view, order_summary_view, payment, payment_status_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new_order/', new_order_view,  name='new_order'),
    path('order_summary/<int:id>', order_summary_view, name='order_summary'),
    path('order_summary/payment/<int:id>', payment, name='summary_payment'),
    path('payment_status/<int:id>', payment_status_view, name='payment_status'),
    path('payment_status/payment/<int:id>', payment, name='try_new_payment') 
    
]

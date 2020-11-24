from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/<int:shopId>/', OrderItemShopAPIView.as_view()),
    path('orderItem/<int:orderItemId>/', OrderItemAPIView.as_view()),
    path('orderItem/create/', OrderItemAPIView.as_view()),
    path('orderItem/', OrderItemsAPIView.as_view()),
    path('orderItem/description/<str:shippingId>/', OrderDescriptionAPIView.as_view()),
    path('carrier/', CarrierAPIView.as_view()),
]

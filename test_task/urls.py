from test_task import views
from django.urls import path

urlpatterns = [
    path('item/<int:pk>/', views.ItemDetailView.as_view(), name='item_detail'),
    path('buy/<int:pk>/', views.CreateCheckoutSessionView.as_view(), name='buy'),
    path('order/<int:pk>/', views.OrdersDetailView.as_view(), name='order_detail'),
    path('order_buy/<int:pk>/', views.OrdersCreateCheckoutSessionView.as_view(), name='order_buy'),
    path('cancel/', views.CancelView.as_view(), name='cancel'),
    path('success/', views.SuccessView.as_view(), name='success'),
]

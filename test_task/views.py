from django.views.generic import DetailView, TemplateView
from django.views import View
from django.http import JsonResponse
import stripe
from django.conf import settings
from .models import *


stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessView(TemplateView):
    """Представление успеха"""
    template_name = 'success.html'


class CancelView(TemplateView):
    """Представление отмены"""
    template_name = 'cancel.html'


class ItemDetailView(DetailView):
    """Представление пункта"""
    model = Item
    template_name = 'item_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        context.update({
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
        })
        return context


class CreateCheckoutSessionView(View):
    """Представление создания сессии Stripe для Item"""
    def get(self, request, *args, **kwargs):
        item_id = self.kwargs['pk']
        item = Item.objects.get(id=item_id)
        your_domain = 'http://127.0.0.1:8000'
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': item.currency,
                        'unit_amount': int(item.get_display_price()[:-3]) * 100,
                        'product_data': {
                            'name': item.name,
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                "item_id": item.id
            },
            mode='payment',
            success_url=your_domain + '/success/',
            cancel_url=your_domain + '/cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })


class OrdersDetailView(DetailView):
    """Представление заказа"""
    model = Orders
    template_name = 'orders_detail.html'

    def get_context_data(self, **kwargs):
        context = super(OrdersDetailView, self).get_context_data(**kwargs)
        context.update({
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
        })
        return context


class OrdersCreateCheckoutSessionView(View):
    """Представление создания сессии Stripe для Order"""
    def get(self, request, *args, **kwargs):
        order_id = self.kwargs['pk']
        order = Orders.objects.get(id=order_id)
        your_domain = 'http://127.0.0.1:8000'
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': order.currency,
                        'unit_amount': order.order_price(),
                        'product_data': {
                            'name': order.name,
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                "item_id": order.id
            },
            mode='payment',
            success_url=your_domain + '/success/',
            cancel_url=your_domain + '/cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })

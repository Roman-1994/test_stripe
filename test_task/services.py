
import stripe


def create_checkout_session(obj_id, name, currency, price):
    redirect_url = 'http://127.0.0.1:8000'
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': currency,
                    'unit_amount': price,
                    'product_data': {
                        'name': name,
                    },
                },
                'quantity': 1,
            },
        ],
        metadata={
            "item_id": obj_id
        },
        mode='payment',
        success_url=redirect_url + '/success/',
        cancel_url=redirect_url + '/cancel/',
    )
    return checkout_session

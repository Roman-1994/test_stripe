from django.db import models


class Item(models.Model):
    """Модель пунктов"""
    CURRENCY_CHOICES = (
        ('usd', 'usd'),
        ('rub', 'rub')
    )

    name = models.CharField(max_length=20, verbose_name='Название')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    price = models.IntegerField(default=0, verbose_name='Цена')
    order = models.ForeignKey('Orders', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Заказ',
                              related_name='item')
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True, null=True, verbose_name='Валюта')

    def __str__(self):
        return self.name

    def get_display_price(self):
        if self.currency == 'usd':
            return "{0:.2f}".format(self.price / 100)
        return "{0:.2f}".format(self.price / 100 * 60)

    class Meta:
        verbose_name = 'Пункт'
        verbose_name_plural = 'Пункты'


class Orders(models.Model):
    """Модель заказов"""
    CURRENCY_CHOICES_ORDER = (
        ('usd', 'usd'),
        ('rub', 'rub')
    )

    name = models.CharField(max_length=30, verbose_name='Название')
    currency = models.CharField(choices=CURRENCY_CHOICES_ORDER, max_length=3, blank=True, null=True,
                                verbose_name='Валюта')

    def __str__(self):
        return self.name

    def order_price(self):
        price = []
        order_item = self.item.all()
        if self.currency == 'usd':
            for i in order_item:
                price.append(int(i.price)/100)
        else:
            for i in order_item:
                price.append(int(i.price)*60/100)
        return int(sum(price))*100

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

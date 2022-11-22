# Generated by Django 4.1.3 on 2022-11-21 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_task', '0002_alter_item_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='item',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='item', to='test_task.orders', verbose_name='Заказ'),
        ),
    ]

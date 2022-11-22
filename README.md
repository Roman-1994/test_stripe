# __Тестовое задание__
***
## Реализовать Django + Stripe API бэкенд
~~~
Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
Django Модель Item с полями (name, description, price) 
API с двумя методами:
    1. GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. 
        При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться 
        запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса
    2. GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация 
        о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id},
        получение session_id и далее  с помощью JS библиотеки Stripe происходить редирект на Checkout 
        форму stripe.redirectToCheckout(sessionId=session_id)

Бонусные задачи: 
    1. Запуск используя Docker (Выполнено)
    2. Использование environment variables (Выполнено)
    3. Просмотр Django Моделей в Django Admin панели (Выполнено)
    4. Запуск приложения на удаленном сервере, доступном для тестирования
    5. Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order 
        c общей стоимостью всех Items (Выполнено)
    6. Модели Discount, Tax, которые можно прикрепить к модели Order и связать с соответствующими атрибутами 
        при создании платежа в Stripe - в таком случае они корректно отображаются в Stripe Checkout форме. 
    7. Добавить поле Item.currency, создать 2 Stripe Keypair на две разные валюты и в зависимости от валюты 
        выбранного товара предлагать оплату в соответствующей валюте (Выполнено)
    8. Реализовать не Stripe Session, а Stripe Payment Intent.

~~~
***

### Шаги для запуска проекта:
~~~
1. docker-compose build
2. docker-compose up
3. Выполнить миграции docker-compose exec web python manage.py migrate --noinput
4. Создать супер пользователя docker-compose exec web python manage.py createsuperuser

~~~
## URLS
### GET /item/<int:pk>/
~~~
Простейшая HTML страница с информацией о выбранном 'Item' и кнопка Buy. По нажатию на кнопку Buy происходит запрос 
на '/buy/<int:pk>/'. С помощью JS библиотеки Stripe происходит редирект на Checkout форму.
~~~
### GET /buy/<int:pk>/
~~~
Получение Stripe Session Id для оплаты выбранного 'Item'
~~~
### GET /order/<int:pk>/
~~~
Простейшая HTML страница с информацией о выбранном 'Order' и кнопка Buy. По нажатию на кнопку Buy происходит запрос 
на '/order_buy/<int:pk>/'. С помощью JS библиотеки Stripe происходит редирект на Checkout форму.
~~~
### GET /order_buy/<int:pk>/
~~~
Получение Stripe Session Id для оплаты выбранного 'Order'
~~~
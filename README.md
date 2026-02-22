# Домашнее задание

Создание проекта, работа с моделями и продвинутая настройка админки

## как все это запустить
- накатить все миграции командой: **python manage.py migrate**
- запустить админку командой: **python manage.py shell**
- выбрать данные из базы, например, такуй командой: **Product.objects.filter(id=1)[0].category**
- (ответ должен быть: "продукты питания")
- выйти из админки командой:**exit()**

## для ввода данных использовались следующие команды
- product1 = Product(name='хлеб', description='первый продукт', price=67)
- product1.save()
- category1 = Category(name='продукты питания', description='только съедобное для людей')
- category1.save()
- Product.objects.all().update(category = 1)

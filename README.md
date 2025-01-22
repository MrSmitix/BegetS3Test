Настройки S3 - BegetS3Test/settings.py:127

Окружение: python3 -m venv venv && . venv/bin/activate && pip install -r requirements.txt
Миграции: ./manage.py migrate
Добавляем админа: ./manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')"
Запуск: ./manage.py runserver

Админка: http://127.0.0.1:8000/admin/
Данные для входа: admin / adminpass

В админке будет 2 модели, Picture и Document. В первую можно грузить только картинки, во вторую всё что угодно. Просто для разнообразия

Для воспроизведения пытаемся добавить новую картинку или документ. После выбора файла жмём сохранить - получаем ошибку

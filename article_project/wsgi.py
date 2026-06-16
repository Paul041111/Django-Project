import os
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "django-insecure-default-key")

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'article_project.settings')

application = get_wsgi_application()
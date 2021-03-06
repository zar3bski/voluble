"""
WSGI config for personal_cms project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personal_cms.settings')

application = get_wsgi_application()

from website.models import Article_category, Photo_category, ExternalAccount, SiteSetting
SiteSetting.load()
Article_category.load()
Photo_category.load()
ExternalAccount.load()

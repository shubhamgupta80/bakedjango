# urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from shop.views import contact_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('page', TemplateView.as_view(template_name='page1.html'), name='page1'),
    path('vendor/login', TemplateView.as_view(template_name='login.html'), name='vendor_login'),
    path('contact', contact_view , name='contact'),
    path('base', TemplateView.as_view(template_name='base.html'), name='base'),
    path('pricing', TemplateView.as_view(template_name='pricing.html'), name='pricing'),
    path('about', TemplateView.as_view(template_name='about.html'), name='about'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
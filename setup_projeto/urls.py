"""
URL configuration for setup_projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import index, salvar_configuracao
from django.views.generic import TemplateView
from core.views import api_palavra_do_dia

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # O caminho vazio '' indica que essa é a página inicial (Home)
    path('salvar-config/', salvar_configuracao, name='salvar_config'), 
    path('sw.js', TemplateView.as_view(template_name="core/sw.js", content_type='application/javascript'), name='sw.js'),
    path('api/palavra/', api_palavra_do_dia, name='api_palavra'),
]  


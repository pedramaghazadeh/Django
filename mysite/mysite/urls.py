"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from editor.views import editor_view, shared_page, login_view, logout_view, su_shared, change_sit
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('change_sit/<int:id>/', change_sit),
    path('su_shared/', su_shared),
    path('login/', login_view),
    path('logout/', logout_view),
    path('', editor_view),
    path('shared/', shared_page),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

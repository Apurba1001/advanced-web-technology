"""
URL configuration for Lab2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from Cat import views as catviews
from Upload import views as upviews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('display/', catviews.Task_getData),
    path('display/<int:id>/', catviews.Task_getData),
    path('delete/<int:id>/', catviews.Task_deleteItem),
    path('Data/', upviews.Document_getData ),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

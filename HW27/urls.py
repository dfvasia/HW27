"""HW27 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from ads.views import MainView, CatDetailView, CatCreateView, CatUpdateView, CatDeleteView, CatListView
from user_continued.views import UserView, UserDetailView, UserUpdateView, UserDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view()),
    path('ad/', include('ads.urls')),
    path('cat/', CatListView.as_view()),
    path('users/', UserView.as_view()),
    path('users/create/', UserView.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view()),
    path('users/<int:pk>/update/', UserUpdateView.as_view()),
    path('users/<int:pk>/delete/', UserDeleteView.as_view()),
    path('cat/create/', CatCreateView.as_view()),
    path('cat/<int:pk>/', CatDetailView.as_view()),
    path('cat/<int:pk>/update/', CatUpdateView.as_view()),
    path('cat/<int:pk>/delete/', CatDeleteView.as_view()),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

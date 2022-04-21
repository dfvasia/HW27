from django.urls import path

from ads import views

urlpatterns = [
    path('', views.AdsView.as_view()),
    path('create/', views.AdsCreateView.as_view()),
    path('<int:pk>/', views.AdsDetailView.as_view()),
    path('<int:pk>/update/', views.AdsUpdateView.as_view()),
    path('<int:pk>/delete/', views.AdsDeleteView.as_view()),
]

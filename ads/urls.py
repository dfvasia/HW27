from django.urls import path


from user_continued.views import UserView, UserDetailView, UserUpdateView, UserDeleteView, UserAdsView, UserCreateView

urlpatterns = [
    path('', UserView.as_view()),
    path('create/', UserView.as_view()),
    path('<int:pk>/', UserCreateView.as_view()),
    path('<int:pk>/update/', UserUpdateView.as_view()),
    path('<int:pk>/delete/', UserDeleteView.as_view()),
    path('<int:pk>/z/', UserAdsView.as_view()),
]

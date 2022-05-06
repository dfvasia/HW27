from django.urls import path


from authentication.views import UserAdsView

# urlpatterns = [
#     path('', UserView.as_view()),
#     path('create/', UserCreateView.as_view()),
#     path('<int:pk>/', UserDetailView.as_view()),
#     path('<int:pk>/update/', UserUpdateView.as_view()),
#     path('<int:pk>/delete/', UserDeleteView.as_view()),
#     path('<int:pk>/z/', UserAdsView.as_view()),
# ]
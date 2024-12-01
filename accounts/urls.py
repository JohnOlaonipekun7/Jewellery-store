from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import SignUpView, ManagerSignUpView,  ProfileDetailView

app_name = 'accounts'

urlpatterns = [
    path('create/', SignUpView.as_view(), name='signup'),
    path('m_signup/', ManagerSignUpView.as_view(), name='msignup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='shop:all_products'), name='logout'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'),
]

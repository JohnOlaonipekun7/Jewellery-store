from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import SignUpView

app_name = 'accounts'

urlpatterns = [
    path('create/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='shop:all_products'), name='logout'),
]

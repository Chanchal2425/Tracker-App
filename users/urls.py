from django.urls import path
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', user_views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),

    path('logout/', user_views.logout_view, name="logout"),
]




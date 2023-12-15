from django.contrib import admin

from app.currency.views import IndexView, ProfileView

from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/', include('django.contrib.auth.urls')),

    path('auth/profile/', ProfileView.as_view(), name='profile'),

    path('', include('app.currency.urls')),

    path('', IndexView.as_view(), name='Index'),

    # Сброс пароля
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]




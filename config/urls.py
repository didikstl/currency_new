from django.contrib import admin

from app.currency.views import IndexView, ProfileView

from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/', include('django.contrib.auth.urls')),
    path('auth/profile/',  include('account.urls')),

    path('', include('app.currency.urls')),
    path('', IndexView.as_view(), name='Index'),

    # Сброс пароля
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
from django.contrib import admin
# from django.urls import path, include
# from app.currency.views import tets_templates, IndexView
# from django.contrib.auth import views as auth_views
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#
#     path('auth/', include('django.contrib.auth.urls')),
#     path('auth/profile/', include('account.urls')),
#
#
#     path('', include('app.currency.urls')),
#     path('template/', tets_templates),
#     path('', IndexView.as_view(), name='Index'),
#
#     path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
#     path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
#     path('reset/<uid64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#     path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
#
# ]



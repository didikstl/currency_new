from django.contrib import admin

from app.currency.views import IndexView, ProfileView

from django.urls import path, include
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from app.currency.views import HomePageView


urlpatterns = [
                  path('admin/', admin.site.urls),

                  path('auth/', include('django.contrib.auth.urls')),
                  path('auth/', include('account.urls')),

                  path('', include('app.currency.urls')),
                  path('', IndexView.as_view(), name='Index'),

                  path('', HomePageView.as_view(), name='home'),



                  # Сброс пароля
                  path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
                  path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
                  path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
                       name='password_reset_confirm'),
                  path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.contrib import admin

from app.currency.views import IndexView, ProfileView

from django.urls import path, include
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
# from app.currency.views import HomePageView, test_view
from app.currency.views import HomePageView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Currency API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
                  path('admin/', admin.site.urls),

                  path('auth/', include('django.contrib.auth.urls')),
                  path('auth/', include('account.urls')),

                  path('', include('app.currency.urls')),

                  path('api/currency/', include('app.currency.api.urls')),

                  path('api/account/', include('account.api.urls')),

                  path('', IndexView.as_view(), name='Index'),
                  # path('test/', test_view),

                  path('', HomePageView.as_view(), name='home'),
                  # документация
                  path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
                  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

                  # Сброс пароля
                  path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
                  path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
                  path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
                       name='password_reset_confirm'),
                  path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

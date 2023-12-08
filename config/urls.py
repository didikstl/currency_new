from django.contrib import admin
from django.urls import path, include

from app.currency.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('app.currency.urls')),

    path('', IndexView.as_view()),

]

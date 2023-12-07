# from django.contrib import admin
# from django.urls import path
# from config.views import index
#
# urlpatterns = [
#     path('', index, name='index'),
#     path('admin/', admin.site.urls),
#
# ]
# from django.conf import settings
# from django.contrib.staticfiles import views
# from django.urls import re_path
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
from django.urls import path, include

from app.currency.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('app.currency.urls')),

    path('', IndexView.as_view()),

    # path("__debug__/", include("debug_toolbar.urls")),
]

# urlpatterns += staticfiles_urlpatterns()
#
# if settings.DEBUG:
#     urlpatterns += [
#         re_path(r"^static/(?P<path>.*)$", views.serve),
#     ]

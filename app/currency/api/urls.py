# from django.urls import path
# from app.currency.api.views import RateListAPIView, RateDetailsAPIView

from app.currency.api.views import RateViewSet, SourceViewSet, ContactUsViewSet

from rest_framework import routers

router = routers.SimpleRouter(trailing_slash=True)
router.register(r'rates', RateViewSet, basename='rate')
router.register(r'source', SourceViewSet, basename='source')
router.register(r'contactus', ContactUsViewSet, basename='contactus')

app_name = 'currency_api'

urlpatterns = router.urls

# urlpatterns = [
#
#     # path('rates/', RateListAPIView.as_view(), name='rate-list'),
#     # path('rates/<int:pk>/', RateDetailsAPIView.as_view(), name='rate-details'),
#
# ] + router.urls

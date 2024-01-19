# from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.viewsets import ModelViewSet

from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer
from rest_framework_yaml.renderers import YAMLRenderer

from app.currency.api.paginator import RatePagination, SourcePagination, ContactUsPagination
from app.currency.api.serializers import RateSerializer, SourceSerializer, ContactUsSerializer
from app.currency.filters import RateFilter, SourceFilter, ContactUsFilter
from app.currency.models import Rate, Source, ContactUs

from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter

from rest_framework import filters


class RateViewSet(ModelViewSet):
    queryset = Rate.objects.all().order_by('-created')
    serializer_class = RateSerializer
    renderer_classes = (JSONRenderer, XMLRenderer, YAMLRenderer)
    pagination_class = RatePagination
    filterset_class = RateFilter
    filter_backends = (
        DjangoFilterBackend,
        # OrderingFilter,
    )


class SourceViewSet(ModelViewSet):
    queryset = Source.objects.all().order_by('-created')
    serializer_class = SourceSerializer
    renderer_classes = (JSONRenderer, XMLRenderer, YAMLRenderer)
    pagination_class = SourcePagination
    filterset_class = SourceFilter
    filter_backends = (
        DjangoFilterBackend,
    )


class ContactUsViewSet(ModelViewSet):
    queryset = ContactUs.objects.all().order_by()
    serializer_class = ContactUsSerializer
    renderer_classes = (JSONRenderer, XMLRenderer, YAMLRenderer)
    pagination_class = ContactUsPagination
    filterset_class = ContactUsFilter
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email']

# class RateListAPIView(ListAPIView):
#     """
#     Получение данных по API от модели Rate
#     """
#     queryset = Rate.objects.all().order_by('-created')
#     # QuerySet - это концепция в Django, представляющая собой набор объектов модели базы данных, на котором можно
#     # выполнять различные запросы. Он предоставляет интерфейс для взаимодействия с базой данных и извлечения данных.
#     # Результаты будут отсортированы по полю created в убывающем порядке (от новых к старым)
#     serializer_class = RateSerializer
#     # Эта строка устанавливает атрибут serializer_class и указывает, что для сериализации данных
#     # (преобразования объектов Rate в формат JSON или другой формат данных) должен использоваться RateSerializer.
#     renderer_classes = (JSONRenderer, XMLRenderer, YAMLRenderer)
#     # Определяет, какие рендереры (форматы вывода) поддерживаются для представления RateListAPIView.
#     # Рендереры отвечают за преобразование данных в определенный формат при формировании HTTP-ответа
#
#
# class RateDetailsAPIView(RetrieveUpdateDestroyAPIView):
#     """
#     Все CRUD операции кроме POST
#     """
#     queryset = Rate.objects.all().order_by('-created')
#     serializer_class = RateSerializer
#     renderer_classes = (JSONRenderer, XMLRenderer, YAMLRenderer)

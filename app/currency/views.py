import re
import requests
import json
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail

from django.views.generic import (
    ListView, CreateView, UpdateView,
    DeleteView, DetailView, TemplateView)

from django_filters.views import FilterView
from django.urls import reverse, reverse_lazy

from app.currency.filters import RateFilter, ContactUsFilter, SourceFilter
from app.currency.forms import RateForm, MessageForm, SourceForm
from app.currency.models import Rate, ContactUs, Source

from django.conf import settings

from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.http import HttpResponse
# для работы с rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views import View
# from django.db import IntegrityError
# from django.shortcuts import render, redirect
# from django.urls import reverse_lazy

#


# RATE _______________________________________________________________________________________

class RateListView(LoginRequiredMixin, FilterView):
    queryset = Rate.objects.all()
    template_name = 'rate_list.html'
    paginate_by = 30
    filterset_class = RateFilter

    # filterset_fields = (
    #     'buy',
    #     'sell',
    #     'type',
    # )

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        Разрешение конфликта между пагинацией и фильтрацией
        :param object_list:
        :param kwargs:
        :return:
        """
        context = super().get_context_data(object_list=object_list, **kwargs)
        query_parameters = self.request.GET.urlencode()

        # первый вариант
        # context['filter_params'] = '&'.join(
        #     f'{key}={value}' for key, value in self.request.GET.items()
        #     if key != 'page'
        # )

        # второй вариант
        context['filter_params'] = re.sub(r'page=\d+', '', query_parameters).lstrip('&')

        return context

    def get_object(self, queryset=None):
        qs = self.get_queryset()
        return qs.get(id=self.request.user.id)


class RateCreateView(CreateView):
    form_class = RateForm
    success_url = reverse_lazy('rate-list')
    template_name = 'rate_create.html'


class RateUpdateView(UserPassesTestMixin, UpdateView):
    model = Rate
    form_class = RateForm
    success_url = reverse_lazy('rate-list')
    template_name = 'rate_update.html'

    def test_func(self):
        # Проверка, является ли текущий пользователь суперпользователем
        return self.request.user.is_superuser

    def handle_no_permission(self):
        # Обработка случая, когда доступ запрещен
        return HttpResponseForbidden("Доступ изменения данных для данного пользователя запрещен.")


class RateDeleteView(UserPassesTestMixin, DeleteView):
    model = Rate
    success_url = reverse_lazy('rate-list')
    template_name = 'rate_delete.html'

    def test_func(self):
        # Проверка, является ли текущий пользователь суперпользователем
        return self.request.user.is_superuser

    def handle_no_permission(self):
        # Обработка случая, когда доступ запрещен
        return HttpResponseForbidden("Доступ удаления данных  для данного пользователя запрещен.")


class RateDetailView(DetailView):
    model = Rate
    template_name = 'rate_details.html'


# MESSAGE_________________________________________________________________________________________

class MessageListView(FilterView):
    queryset = ContactUs.objects.all()
    template_name = 'message_list.html'
    paginate_by = 5
    filterset_class = ContactUsFilter

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        Разрешение конфликта между пагинацией и фильтрацией
        :param object_list:
        :param kwargs:
        :return:
        """
        context = super().get_context_data(object_list=object_list, **kwargs)
        query_parameters = self.request.GET.urlencode()
        context['filter_params'] = '&'.join(
            f'{key}={value}' for key, value in self.request.GET.items()
            if key != 'page'
        )

        return context


class MessageCreateView(CreateView):
    form_class = MessageForm
    success_url = reverse_lazy('message-list')
    template_name = 'message_list_create.html'

    def _send_email(self):
        recipient = settings.DEFAULT_FROM_EMAIL,
        subject = "User contact us",
        message = f"""
                    Name: {self.object.name}
                    Email: {self.object.email}
                    Subject: {self.object.subject}
                    Message: {self.object.message}
                    """
        send_mail(
            subject,
            message,
            recipient,
            [recipient],
            fail_silently=False,
        )

    def form_valid(self, form):
        redirect = super().form_valid(form)
        self._send_email()
        return redirect


class MessageUpdateView(UpdateView):
    model = ContactUs
    form_class = MessageForm
    success_url = reverse_lazy('message-list')
    template_name = 'message_list_update.html'


class MessageDeleteView(DeleteView):
    model = ContactUs
    success_url = reverse_lazy('message-list')
    template_name = 'message_list_delete.html'


class MessageDetailView(DetailView):
    model = ContactUs
    template_name = 'message_details.html'


# SOURCE___________________________________________________________________________________________

class SourceListView(FilterView):
    queryset = Source.objects.all()
    template_name = 'source_list.html'
    paginate_by = 5
    filterset_class = SourceFilter

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        Разрешение конфликта между пагинацией и фильтрацией
        :param object_list:
        :param kwargs:
        :return:
        """
        context = super().get_context_data(object_list=object_list, **kwargs)
        query_parameters = self.request.GET.urlencode()
        context['filter_params'] = '&'.join(
            f'{key}={value}' for key, value in self.request.GET.items()
            if key != 'page'
        )

        return context
    # fields = ('Logo')


class SourceCreateView(CreateView):
    form_class = SourceForm
    success_url = reverse_lazy('source-list')
    template_name = 'source_create.html'




class SourceUpdateView(UpdateView):
    model = Source
    form_class = SourceForm
    success_url = reverse_lazy('source-list')
    template_name = 'source_update.html'

    # def form_valid(self, form):
    #     # Проверяем, существует ли объект с таким code_name
    #     if Source.objects.filter(code_name=form.cleaned_data['code_name']).exists():
    #         # Обработка ситуации, когда объект уже существует
    #         from pyexpat.errors import messages
    #         messages.error(self.request, 'This code name already exists. Please choose a different one.')
    #         return render(self.request, self.template_name, {'form': form})
    #
    #     # Если объекта с таким code_name нет, продолжаем сохранение
    #     return super().form_valid(form)

class SourceDeleteView(DeleteView):
    model = Source
    success_url = reverse_lazy('source-list')
    template_name = 'source_delete.html'


class SourceDetailView(DetailView):
    model = Source
    template_name = 'source_details.html'


# BASE Index ____________________________________________________________________

class IndexView(TemplateView):
    template_name = 'index.html'


# ProfifeView_____________________________________________________________________


class ProfileView(LoginRequiredMixin, UpdateView):
    """
        Для регистрации пользователя, запроса логина и пароля
    """
    model = get_user_model()
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('Index')
    fields = (
        'first_name',
        'last_name',
    )

    def get_object(self, queryset=None):
        """
        Возврат данных пользователя по ИД.
        :param queryset:
        :return:
        """
        qs = self.get_queryset()
        return qs.get(id=self.request.user.id)


# _____________________________________________

class HomePageView(TemplateView):
    template_name = 'home.html'


# _________Тестовая____________________________________
# @api_view(['GET'])
# def test_view(request):
#     object_list = Rate.objects.all()
#     context = []
#
#     for obj in object_list:
#         context.append({
#             'id': obj.id,
#             'buy': float(obj.buy),
#             'sell': float(obj.sell),
#         })
#
#     # headers = {
#     #     'Content-Type': 'application/json'
#     # }
#
#     # return HttpResponse(json.dumps(context), headers=headers)
#     return Response(context)
#________Django_REST_framework_______________________________

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail

from django.views.generic import (
    ListView, CreateView, UpdateView,
    DeleteView, DetailView, TemplateView)

from django.urls import reverse, reverse_lazy

from app.currency.forms import RateForm, MessageForm, SourceForm
from app.currency.models import Rate, ContactUs, Source

from django.conf import settings


from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.views import View

#


# RATE _______________________________________________________________________________________

class RateListView(LoginRequiredMixin, ListView):
    queryset = Rate.objects.all()
    template_name = 'rate_list.html'

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

class MessageListView(ListView):
    queryset = ContactUs.objects.all()
    template_name = 'message_list.html'


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

class SourceListView(ListView):
    queryset = Source.objects.all()
    template_name = 'source_list.html'


class SourceCreateView(CreateView):
    form_class = SourceForm
    success_url = reverse_lazy('source-list')
    template_name = 'source_create.html'


class SourceUpdateView(UpdateView):
    model = Source
    form_class = SourceForm
    success_url = reverse_lazy('source-list')
    template_name = 'source_update.html'


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
    model = get_user_model()
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('Index')
    fields = (
        'first_name',
        'last_name',
    )

    # def get_queryset(self):
    #     qs = super().get_queryset().filter(id=self.request.user.id)
    #     return qs


    def get_object(self, queryset=None):
        qs = self.get_queryset()
        return qs.get(id=self.request.user.id)
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from app.currency.forms import RateForm, MessageForm, SourceForm
from app.currency.models import Rate, ContactUs, Source
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView


# RATE _______________________________________________________________________________________

class RateListView(ListView):
    queryset = Rate.objects.all()
    template_name = 'rate_list.html'


class RateCreateView(CreateView):
    form_class = RateForm
    success_url = reverse_lazy('rate-list')
    template_name = 'rate_create.html'


class RateUpdateView(UpdateView):
    model = Rate
    form_class = RateForm
    success_url = reverse_lazy('rate-list')
    template_name = 'rate_update.html'


class RateDeleteView(DeleteView):
    model = Rate
    success_url = reverse_lazy('rate-list')
    template_name = 'rate_delete.html'


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


# BASE ____________________________________________________________________

class IndexView(TemplateView):
    template_name = 'index.html'

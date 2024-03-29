from django.views.generic import CreateView, UpdateView, RedirectView
from account.forms import UserSignUpForm

from django.urls import reverse_lazy

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

User = get_user_model()


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('Index')
    fields = (
        'first_name',
        'last_name',
        'avatar',
        'email',
        'phone',
    )

    def get_object(self, queryset=None):
        qs = self.get_queryset()
        return qs.get(id=self.request.user.id)


class UserSignUpView(CreateView):
    queryset = User.objects.all()
    template_name = 'signup.html'
    success_url = reverse_lazy('Index')
    form_class = UserSignUpForm


class UserActivateView(RedirectView):
    pattern_name = 'login'

    def get_redirect_url(self, *args, **kwargs):
        username = kwargs.pop('username')

        user = User.objects.filter(username=username).only('id').first()

        if user is not None:

            user.is_active = True
            user.save(update_fields=('is_active'))

        return super().get_redirect_url(*args, **kwargs)
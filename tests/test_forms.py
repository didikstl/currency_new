# import pytest
# from django.urls import reverse
# from django.core import mail
# from django.contrib.auth import get_user_model
# from django.test import RequestFactory
# from account.forms import UserSignUpForm
# # from account.views import activate_account
#
# User = get_user_model()
#
#
# @pytest.fixture
# def user_data():
#     return {
#         'email': 'test@example.com',
#         'password1': 'securepassword',
#         'password2': 'securepassword',
#     }
#
#
# @pytest.fixture
# def request_factory():
#     return RequestFactory()
#
#
# def test_user_signup_form_valid(user_data):
#     form = UserSignUpForm(data=user_data)
#     assert form.is_valid()


# def test_user_signup_form_invalid_passwords(user_data):
#     user_data['password2'] = 'differentpassword'
#     form = UserSignUpForm(data=user_data)
#     assert not form.is_valid()
#     assert '__all__' in form.errors
#     assert 'Passwords should match' in form.errors['__all__']
    # assert 'password2' in form.errors


# def test_user_signup_form_save(user_data, mocker):
#     mocker.patch('account.forms.send_mail')
#     form = UserSignUpForm(data=user_data)
#     assert form.is_valid()

    # user = form.save()
    #
    # assert user.email == user_data['email']
    # assert user.check_password(user_data['password1'])
    # assert not user.is_active

    # Проверяем, что отправлено письмо
    # mocker.patch('django.core.mail.send_mail')
    # assert mail.outbox[0].subject == 'Thanks for signing up'
    # assert user_data['email'] in mail.outbox[0].to[0]


# def test_user_signup_form_activation_email_content(user_data, mocker):
#     mocker.patch('account.forms.send_mail')
#     form = UserSignUpForm(data=user_data)
#     assert form.is_valid()
    #
    # form.save()
    #
    # mocker.patch('django.core.mail.send_mail')
    # assert 'activate' in mail.outbox[0].body
    # assert reverse('account:activate', args=(form.instance.username,)) in mail.outbox[0].body


# def test_activate_account_view(client, user_data, mocker):
#     mocker.patch('account.forms.User.objects.get')
#     user = User.objects.create(email=user_data['email'], is_active=False)
#     activate_path = reverse('account:activate', args=(user.username,))
#     response = client.get(activate_path)
#     assert response.status_code == 200
#
#     # Проверяем, что пользователь активирован
#     assert User.objects.get(username=user.username).is_active
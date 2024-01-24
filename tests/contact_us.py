from django.urls import reverse


def test_post_contact_us_empty_form(client):
    response = client.post(reverse('message-create'))
    assert response.status_code == 200

# def test_post_contact_us_empty_form(client):
#     response = client.post('/message/create/')
#     assert response.status_code == 200

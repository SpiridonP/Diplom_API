import allure
import requests
from test_urls import change_user
from payloads.change_user_payload import password_change
from payloads.change_user_payload import email_change
import test_headers
import data_answers


class TestChangeData:

    @allure.title('Изменение пароля')
    @allure.step('В теле запроса указать новый пароль и отправить запрос (в параметрах добавить авторизацию пользователя)')
    def test_change_password(self):
        header = test_headers.headers
        payload = password_change
        response = requests.patch(change_user, data=payload, headers=header)
        assert response.status_code == 200 and "success" in response.json()

    @allure.title('Изменение email')
    @allure.step('В теле запроса указать email и отправить запрос (в параметрах добавить авторизацию пользователя)')
    def test_change_email(self):
        header = test_headers.headers
        payload = email_change
        response = requests.patch(change_user, data=payload, headers=header)
        assert response.status_code == 200 and "success" in response.json()

    @allure.title('Изменение пароля')
    @allure.step('В теле запроса указать пароль и отправить запрос (в параметрах не добавлять авторизацию пользователя)')
    def test_change_password_not_auth(self):
        payload = password_change
        response = requests.patch(change_user, data=payload)
        assert response.status_code == 401 and response.json() == data_answers.not_auth

    @allure.title('Изменение email')
    @allure.step('В теле запроса указать email и отправить запрос (в параметрах не добавлять авторизацию пользователя)')
    def test_change_email_not_auth(self):
        payload = email_change
        response = requests.patch(change_user, data=payload)
        assert response.status_code == 401 and response.json() == data_answers.not_auth





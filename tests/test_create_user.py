import requests
from test_urls import create_user
from payloads.create_user_payload import create
from payloads.create_user_payload import no_password
import data_answers
import allure


class TestCreateUser:

    @allure.title('Создание пользователя')
    @allure.step('В теле запроса указать обязательные поля для создания пользователя')
    def test_first_create(self):
        payload = create
        response = requests.post(create_user, data=payload)
        assert response.status_code == 200

    @allure.title('Создание пользователя с существующими данными')
    @allure.step('В теле запроса указать данные существующего пользователя')
    def test_user_exists(self):
        payload = create
        response = requests.post(create_user, data=payload)
        assert response.status_code == 403 and response.json() == data_answers.answer_exist_user

    @allure.title('Создание пользователя без пароля')
    @allure.step('В теле запроса не указать пароль')
    def test_no_password(self):
        payload = no_password
        response = requests.post(create_user, data=payload)
        assert response.status_code == 403 and response.json() == data_answers.answer_not_required_field
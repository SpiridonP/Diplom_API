import requests
from urls import log_in
from payloads.log_in_payload import user
from payloads.log_in_payload import incorrect_login
import data_answers
import allure




class TestLogIn:

    @allure.title('Авторизация пользователя')
    @allure.step('В телезапроса указать данные для авторизации')
    def test_log_in_correct(self):
        payload = user
        response = requests.post(log_in, data=payload)
        assert response.status_code == 200 and "refreshToken" in response.json()

    @allure.title('Авторизация пользователя с некорректными данными')
    @allure.step('В телезапроса указать некорректный логин')
    def test_incorrect_login(self):
        payload = incorrect_login
        response = requests.post(log_in, data=payload)
        assert response.status_code == 401 and response.json() == data_answers.incorrect_auth



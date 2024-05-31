import requests
from test_urls import create_burger
from payloads.create_burger_payload import burger_1
from payloads.create_burger_payload import burger_2
from payloads.create_burger_payload import burger_3
from payloads.create_burger_payload import burger_4
import test_headers
import data_answers
import allure

class TestCreateBurger:

    @allure.title('Создание заказа авторизованным пользователем')
    @allure.step('В параметрах к запросу авторизовать пользователя и в теле запроса указать корректные данные')
    def test_create_order_with_auth(self):
        header = test_headers.headers
        payload = burger_1
        response = requests.post(create_burger, data=payload, headers=header)
        assert response.status_code == 200

    @allure.title('Создание заказа неавторизованным пользователем')
    @allure.step('В параметрах к запросу ничего не указывать и в теле запроса указать корректные данные')
    def test_create_order_without_auth(self):
        payload = burger_2
        response = requests.post(create_burger, data=payload)
        assert response.status_code == 200

    @allure.title('Заказ без ингредиентов')
    @allure.step('В параметрах к запросу авторизовать пользователя и в теле запроса не указать ингредиенты')
    def test_without_ingredients(self):
        header = test_headers.headers
        payload = burger_3
        response = requests.post(create_burger, data=payload, headers=header)
        assert response.status_code == 400 and response.json() == data_answers.no_ingredients

    @allure.title('Указать некорректный хэш ингредиентов')
    @allure.step('В параметрах к запросу авторизовать пользователя и в теле запроса указать некорректный хэш ингредиентов')
    def test_incorrect_hash(self):
        header = test_headers.headers
        payload = burger_4
        response = requests.post(create_burger, data=payload, headers=header)
        assert response.status_code == 500

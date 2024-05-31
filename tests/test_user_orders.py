import requests
import test_headers
import data_answers
from test_urls import get_orders
import allure


class TestGetOrders:

    @allure.title('Получение заказов пользователя')
    @allure.step('В параметрах авторизовать пользователя')
    def test_auth_user(self):
        header = test_headers.headers
        response = requests.get(get_orders, headers=header)
        assert 'success' in response.json()

    @allure.title('Получение заказов неавторизованного пользователя')
    @allure.step('Не указать параметры авторизации')
    def test_not_auth_user(self):
        response = requests.get(get_orders)
        assert response.status_code == 401 and response.json() == data_answers.get_not_uat_user_order
import requests


# использовать pytest

def test_successful_request():
    response = requests.get("https://petstore.swagger.io/v2/pet/1")
    assert response.status_code == 200, "Код состояния: 200"
    print("Успешный запрос: статус код 200")


def test_successful_response_format():
    response = requests.get("https://petstore.swagger.io/v2/pet/1")
    assert response.headers["Content-Type"] == "application/json", "Формат данных: JSON"
    print("Успешный запрос: формат данных JSON")


def test_invalid_request():
    response = requests.get("https://petstore.swagger.io/v2/pet/invalid_id")
    assert response.status_code == 404, "Код состояния: 404"
    print("Запрос с неверными параметрами: статус код 404")


def test_invalid_response_format():
    response = requests.get("https://petstore.swagger.io/v2/pet/invalid_id")
    assert response.headers["Content-Type"] == "application/json", "Формат данных: JSON"
    print("Запрос с неверными параметрами: формат данных JSON")


def test_invalid_parameters():
    response = requests.get("https://petstore.swagger.io/v2/pet/999999999")
    assert response.status_code == 404, "Код состояния: 404"
    print("Запрос с недопустимыми параметрами: статус код 404")

# Юлия Синицына, 6-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request


def test_code():
    # Проверяется, что код ответа равен 200
    assert sender_stand_request.response.status_code == 200

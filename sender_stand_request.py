import configuration
import requests
import data


# создаем новый заказ
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.order_body)


def save_track():
    order_response = post_new_order()
    current_order = order_response.json().copy()
    current_order["t"] = current_order["track"]
    current_order.pop("track")
    return current_order


# запрос на получение заказа по треку
def get_order_by_track():
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK,
                        params=save_track())


response = get_order_by_track()

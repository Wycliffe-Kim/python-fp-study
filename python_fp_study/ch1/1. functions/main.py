from backend import Backend

backend = Backend()


def f(x: int):
    return x * 2


def fetch_data_from_db(api: str):
    data = backend.fetch(api)
    return data


def fetch_data_from_db(backend: Backend, api: str):
    data = backend.fetch(api)
    return data

import pytest
from homework_14.store.store_facade import StoreFacade


@pytest.fixture(name='add_phone')
def store_facade(request):
    store = StoreFacade()
    phone_info = request.param
    if phone_info:
        store.add_phone_to_catalog(*phone_info)
    yield store, str(store.show_catalog()[0])
    del store.catalog.phones


@pytest.fixture(autouse=True, scope='class')
def store_facade_cls(request):
    store = StoreFacade()
    request.cls.store = store
    yield
    del store.catalog.phones


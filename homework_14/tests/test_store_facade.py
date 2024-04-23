import pytest


class TestStore:
    def test_get_empty_catalog(self):
        catalog = self.store.show_catalog()
        assert not catalog
        assert isinstance(catalog, list)

    @pytest.mark.parametrize('add_phone', [('Lenovo', 3500)], indirect=True)
    def test_add_phone_to_catalog(self, add_phone):
        store, phone_info = add_phone
        phone_list = str(store.show_catalog()[0])
        assert phone_list, f"Parameter {phone_info} was not added to the catalog"
        assert phone_info == phone_list, f"Added parameter is not equal to the result list"

    @pytest.mark.linked
    @pytest.mark.parametrize('brand, price', [('Lenovo', 3600), ('iPhone', 4000), ('Mac', 10000)])
    def test_add_several_phones_to_catalog(self, brand, price):
        phone = self.store.add_phone_to_catalog(brand, price)
        result_list = self.store.show_catalog()
        assert phone in result_list, f"Phone '{phone}' was not added to the catalog"

    @pytest.mark.linked
    @pytest.mark.parametrize('brand', ['Mac'])
    def test_remove_phone_from_catalog(self, brand):
        list_len_before_remove = len(self.store.show_catalog())
        self.store.remove_phone_from_catalog(brand)
        list_after_before_remove = len(self.store.show_catalog())
        assert list_len_before_remove > list_after_before_remove , f"'{brand}' was not removed from catalog"

    @pytest.mark.linked
    @pytest.mark.negative
    @pytest.mark.parametrize('brand', ['Asus'])
    def test_remove_non_existing_phone(self, brand):
        with pytest.raises(IndexError) as error:
            result = self.store.remove_phone_from_catalog(brand)
            assert result is None
            assert error.value is 'list index out of range'


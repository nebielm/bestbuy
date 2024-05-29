import pytest
import products


def test_valid_product_creation():
    test_1_product = products.Product("Test1", price=1450, quant=100)
    assert test_1_product.name == "Test1"
    assert test_1_product.price == 1450
    assert test_1_product.quant == 100
    print("Test 1 completed, normal product created")


def test_invalid_details_product():
    with pytest.raises(Exception, match="You have to enter a name."):
        products.Product("", price=1450, quant=100)
    with pytest.raises(Exception, match="The price has to be a positive number."):
        products.Product("Test2", price=-1450, quant=100)
    with pytest.raises(Exception, match="The quantity has to be a positive number."):
        products.Product("Test2", price=1450, quant=0)


def test_is_inactive():
    with pytest.raises(Exception):
        test_3_product = products.Product("Test3", price=1450, quant=100)
        test_3_product.buy(100)
        assert test_3_product.active


def test_correct_purchase():
    with pytest.raises(Exception):
        test_4_product = products.Product("Test3", price=1450, quant=100)
        assert type(test_4_product.buy(50)) != float
        assert test_4_product.quant != 50


def test_no_inventory():
    with pytest.raises(Exception, match="Order quantity not in storage."):
        test_5_product = products.Product("Test3", price=1450, quant=100)
        test_5_product.buy(101)


pytest.main()
